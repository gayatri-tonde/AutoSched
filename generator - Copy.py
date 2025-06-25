import random

def generate_all_timetables(start, end, num_periods, num_breaks, break_durations,
                            classrooms, sections, days, subjects):

    timetable_list = []
    subject_slots = []
    for s in subjects:
        subject_slots.extend([s] * s['freq'])

    def calculate_break_points(periods, num_breaks):
        if num_breaks == 0:
            return []
    
        if num_breaks >= 1:
            # Example: 2 breaks in 8 periods = [2, 6]
            gap = periods // (num_breaks + 1)
            return [gap * i for i in range(1, num_breaks + 1)]
        

    for sec in range(sections):
        timetable = []
        available_slots = subject_slots[:]
        random.shuffle(available_slots)

        for day in days:
            row = []
            slots_in_day = num_periods + num_breaks
            break_points = calculate_break_points(num_periods, num_breaks)
            b_index = 0
            for i in range(slots_in_day):
                if b_index < len(break_points) and i == break_points[b_index]:
                    row.append(f"Break ({break_durations[b_index]} min)")
                    b_index += 1
                elif available_slots:
                    s = available_slots.pop()
                    row.append(f"{s['name']} ({s['faculty']})")
                else:
                    row.append("Free")
            timetable.append(row)
        timetable_list.append(timetable)
    return timetable_list