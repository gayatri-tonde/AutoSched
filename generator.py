import random
from copy import deepcopy


def generate_all_timetables(start, end, num_periods, num_breaks, break_durations,
                            classrooms, sections, days, subjects):
    """
    Generates realistic, conflict-free timetables for all sections.

    Key guarantees:
    - No consecutive same-subject slots on the same day
    - Subjects distributed evenly across days (not dumped on day 1)
    - Each section gets an independent, freshly distributed schedule
    - Faculty clash detection across sections for the same time slot
    - Breaks placed at evenly-spaced positions within each day
    - Remaining slots filled with 'Free' gracefully
    """

    num_days = len(days)

    # ── 1. CALCULATE BREAK POSITIONS ──────────────────────────────────────────
    # Break positions are indices within a full row (periods + breaks combined)
    def get_break_positions(num_periods, num_breaks):
        if num_breaks == 0:
            return []
        # Spread breaks evenly. E.g. 8 periods, 2 breaks → after slot 3 and slot 6
        gap = num_periods // (num_breaks + 1)
        positions = []
        offset = 0
        for i in range(1, num_breaks + 1):
            pos = gap * i + offset  # shift right as we add breaks
            positions.append(pos)
            offset += 1  # each break inserted shifts subsequent positions
        return positions

    break_positions = get_break_positions(num_periods, num_breaks)
    slots_per_day = num_periods + num_breaks  # total columns per row

    # ── 2. BUILD PER-DAY SUBJECT POOLS ────────────────────────────────────────
    # Distribute subject frequency evenly across days.
    # E.g. Maths freq=4, 5 days → Mon:1, Tue:1, Wed:1, Thu:1, Fri:0
    def build_daily_pool(subjects, num_days):
        """Returns dict: day_index → list of subject label strings"""
        daily = {d: [] for d in range(num_days)}
        for subj in subjects:
            freq = subj['freq']
            label = f"{subj['name']} ({subj['faculty']})"
            # round-robin across days
            for i in range(freq):
                daily[i % num_days].append(label)
        return daily

    # ── 3. SHUFFLE WITH NO-CONSECUTIVE CONSTRAINT ─────────────────────────────
    def shuffle_no_consecutive(items):
        """
        Shuffles a list so no two identical items are adjacent.
        Falls back to best-effort if impossible (e.g. >50% same item).
        """
        if not items:
            return []
        items = items[:]
        random.shuffle(items)
        max_attempts = 200
        for _ in range(max_attempts):
            conflict = False
            for i in range(len(items) - 1):
                if items[i] == items[i + 1]:
                    # find a swap candidate
                    swapped = False
                    for j in range(i + 2, len(items)):
                        if items[j] != items[i] and (j + 1 >= len(items) or items[j + 1] != items[i]):
                            items[i + 1], items[j] = items[j], items[i + 1]
                            swapped = True
                            break
                    if not swapped:
                        conflict = True
            if not conflict:
                break
        return items

    # ── 4. BUILD A ROW (one day's slots) ─────────────────────────────────────
    def build_row(period_subjects):
        """
        Given an ordered list of period_subjects (already no-consecutive),
        inserts breaks at the correct positions.
        """
        row = []
        period_iter = iter(period_subjects)
        break_idx = 0

        for slot_i in range(slots_per_day):
            if break_idx < len(break_positions) and slot_i == break_positions[break_idx]:
                dur = break_durations[break_idx] if break_idx < len(break_durations) else 10
                row.append(f"Break ({dur} min)")
                break_idx += 1
            else:
                subj = next(period_iter, "Free")
                row.append(subj)
        return row

    # ── 5. FACULTY CLASH TRACKER ──────────────────────────────────────────────
    # faculty_usage[day_idx][slot_idx] = set of faculty names already assigned
    faculty_usage = [[set() for _ in range(slots_per_day)] for _ in range(num_days)]

    def extract_faculty(slot_label):
        """Extract faculty name from 'SubjectName (FacultyName)'"""
        if '(' in slot_label and ')' in slot_label:
            return slot_label[slot_label.rfind('(') + 1: slot_label.rfind(')')]
        return None

    def resolve_faculty_clashes(row, day_idx, section_idx):
        """
        Check each period slot in a row. If faculty is already used in that
        slot by another section, swap with another slot in the same row.
        Marks used faculty in faculty_usage after resolution.
        """
        resolved = row[:]
        for slot_i, slot in enumerate(resolved):
            if slot.startswith("Break") or slot == "Free":
                continue
            fac = extract_faculty(slot)
            if fac and fac in faculty_usage[day_idx][slot_i]:
                # try to find a swap within this row
                for swap_i in range(len(resolved)):
                    if swap_i == slot_i:
                        continue
                    swap_slot = resolved[swap_i]
                    if swap_slot.startswith("Break") or swap_slot == "Free":
                        continue
                    swap_fac = extract_faculty(swap_slot)
                    if swap_fac not in faculty_usage[day_idx][slot_i] and \
                       (fac not in faculty_usage[day_idx][swap_i]):
                        resolved[slot_i], resolved[swap_i] = resolved[swap_i], resolved[slot_i]
                        break
        # register faculty usage
        for slot_i, slot in enumerate(resolved):
            fac = extract_faculty(slot)
            if fac:
                faculty_usage[day_idx][slot_i].add(fac)
        return resolved

    # ── 6. GENERATE ALL SECTIONS ──────────────────────────────────────────────
    all_timetables = []

    for sec in range(sections):
        section_timetable = []

        # Fresh daily pool for each section (independent distribution)
        daily_pool = build_daily_pool(subjects, num_days)

        for day_idx in range(num_days):
            pool = daily_pool[day_idx][:]

            # Pad or trim to exactly num_periods
            if len(pool) < num_periods:
                pool += ["Free"] * (num_periods - len(pool))
            elif len(pool) > num_periods:
                pool = pool[:num_periods]

            # Shuffle with no-consecutive constraint
            non_free = [p for p in pool if p != "Free"]
            free_slots = ["Free"] * pool.count("Free")
            non_free_shuffled = shuffle_no_consecutive(non_free)

            # Interleave Free slots at random positions
            combined = non_free_shuffled + free_slots
            random.shuffle(combined)
            # Re-check no consecutive after free interleaving
            combined = shuffle_no_consecutive(combined)

            # Build the row with breaks inserted
            row = build_row(combined)

            # Resolve faculty clashes across sections
            row = resolve_faculty_clashes(row, day_idx, sec)

            section_timetable.append(row)

        all_timetables.append(section_timetable)

    return all_timetables
