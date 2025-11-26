# AutoSched – Intelligent Timetable Generator 🗓️

AutoSched is a web-based intelligent timetable generator that automates the creation of conflict-free, multi-section class schedules based on user inputs. It streamlines scheduling for educational institutions by reducing manual effort and optimizing resource allocation.

---

## 🔧 How It Works

1. **User Input Interface** (via web form):
   - Working days
   - Start & end time of each day
   - Number of periods and breaks
   - Classroom and section count
   - Subject details: name, frequency, duration, faculty
   - Custom duration for each break

2. **Timetable Generation Logic**:
   - Evenly distributes subjects across all days and sections
   - Avoids faculty and classroom clashes
   - Ensures uniform break distribution
   - Fills remaining slots with “Free” if needed

3. **Output**:
   - A tabular block-style timetable for each section
   - Breaks shown clearly
   - Subject and faculty shown in each slot

---

## ✨ Features

- 📥 **Multi-page Input Form**
  - Intuitive UI for entering all necessary scheduling data

- ⚙️ **Backend Generation Logic**
  - Dynamically calculates period/break distribution
  - Randomized yet valid subject scheduling with constraints

- 📄 **Timetable Output**
  - Clean tabular format using Flask templates
  - Displays each section’s timetable per day

- 🎯 **Scalable Design**
  - Supports multiple sections and classrooms

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, Bootstrap (in `templates/`)
- **Backend:** Python, Flask (`app.py`)
- **Scheduling Logic:** Python (`generator.py`)
- **Template Engine:** Jinja2
- **Database:** *Not yet implemented, future enhancement*

---
