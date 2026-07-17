# AutoSched – Intelligent Timetable Generator 📅

AutoSched is a web-based intelligent timetable generation system designed to automate the process of creating structured, conflict-free class schedules for educational institutions.

The system takes scheduling requirements such as working days, class timings, subjects, faculty members, sections, classrooms, periods, and breaks as input and automatically generates timetables for multiple sections.

AutoSched aims to reduce the time and effort involved in manually preparing academic timetables while minimizing scheduling conflicts and improving resource allocation.

---

## 🚀 Features

* **Automated Timetable Generation**

  * Automatically generates timetables based on user-provided scheduling requirements.
  * Reduces the need for manual timetable preparation.

* **Multi-Section Scheduling**

  * Supports timetable generation for multiple sections.
  * Generates a separate timetable for each section.

* **Faculty Conflict Management**

  * Helps prevent the same faculty member from being assigned to multiple classes at the same time.

* **Classroom Conflict Management**

  * Avoids assigning the same classroom to multiple sections simultaneously.

* **Subject Distribution**

  * Distributes subjects across available working days and periods.
  * Considers subject frequency and duration while generating the timetable.

* **Custom Break Scheduling**

  * Allows users to define the number and duration of breaks.
  * Breaks are clearly displayed in the generated timetable.

* **Free Period Allocation**

  * Remaining timetable slots can automatically be marked as **Free** when no subject is scheduled.

* **Web-Based Interface**

  * Provides an easy-to-use interface for entering timetable requirements.
  * Displays generated schedules in a clean tabular format.

---

## 🛠️ Tech Stack

| Technology | Purpose                               |
| ---------- | ------------------------------------- |
| Python     | Core application and scheduling logic |
| Flask      | Backend web framework                 |
| HTML       | Web page structure                    |
| CSS        | User interface styling                |
| Bootstrap  | Responsive UI components              |
| Jinja2     | Dynamic HTML template rendering       |

---

## 📂 Project Structure

```text
AutoSched/
│
├── app.py
│   └── Main Flask application
│
├── generator.py
│   └── Contains timetable generation logic
│
├── index.html
│   └── User input interface
│
├── timetable.html
│   └── Displays the generated timetable
│
├── static/
│   └── Static assets such as CSS and other resources
│
├── media files/
│   └── Project-related media resources
│
├── AutoSched.pptx
│   └── Project presentation
│
└── README.md
    └── Project documentation
```

---

## ⚙️ How It Works

### 1. Enter Scheduling Details

The user provides the required timetable configuration through the web interface.

The input may include:

* Number of working days
* Daily start and end time
* Number of periods
* Number of breaks
* Duration of breaks
* Number of classrooms
* Number of sections
* Subject names
* Subject frequency
* Subject duration
* Assigned faculty members

### 2. Process Scheduling Constraints

The backend processes the submitted information and passes it to the timetable generation logic.

The scheduling algorithm attempts to:

* Distribute subjects across available days
* Schedule the required subject frequency
* Avoid faculty clashes
* Avoid classroom conflicts
* Allocate breaks appropriately
* Generate schedules for multiple sections
* Fill unused slots with free periods when necessary

### 3. Generate Timetable

Once scheduling is completed, AutoSched generates a structured timetable for each section.

Each timetable displays:

* Day
* Time/Period
* Subject
* Faculty
* Breaks
* Free periods

---

## 💻 Installation

### Prerequisites

Before running the project, make sure you have the following installed:

* Python 3.x
* pip
* Git

### 1. Clone the Repository

```bash
git clone https://github.com/gayatri-tonde/AutoSched.git
```

### 2. Navigate to the Project Directory

```bash
cd AutoSched
```

### 3. Install Flask

```bash
pip install flask
```

If the project includes a `requirements.txt` file in the future, dependencies can instead be installed using:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open the Application

After starting the Flask development server, open the local address displayed in your terminal, typically:

```text
http://127.0.0.1:5000
```

---

## 📖 Usage

1. Start the Flask application.
2. Open AutoSched in your web browser.
3. Enter the required timetable configuration.
4. Add subject and faculty details.
5. Configure periods and breaks.
6. Submit the scheduling information.
7. The system processes the constraints.
8. View the automatically generated timetable for each section.

---

## 🎯 Project Objective

Creating academic timetables manually can be time-consuming, especially when multiple sections, classrooms, faculty members, subjects, and scheduling constraints are involved.

AutoSched provides an automated approach to timetable generation by processing scheduling requirements and generating organized class schedules while attempting to minimize conflicts.

The project demonstrates how web technologies and scheduling algorithms can be combined to simplify academic resource planning.

---

## 🔮 Future Enhancements

Potential improvements for AutoSched include:

* Database integration for persistent storage
* User authentication and role-based access
* Admin dashboard
* Faculty availability management
* Advanced constraint-satisfaction algorithms
* Priority-based subject scheduling
* Manual timetable editing after generation
* Export timetable to PDF
* Export timetable to Excel
* Download and print functionality
* Email timetable to faculty and students
* Drag-and-drop timetable editing
* Mobile-responsive timetable views
* Automatic detection and reporting of scheduling conflicts
* Cloud deployment

---

## 🤝 Contributing

Contributions are welcome!

To contribute:

1. Fork the repository.
2. Create a new feature branch.

```bash
git checkout -b feature/your-feature-name
```

3. Make your changes.
4. Commit your changes.

```bash
git commit -m "Add your feature"
```

5. Push the branch.

```bash
git push origin feature/your-feature-name
```

6. Open a Pull Request.

---

## 📜 License

This project currently does not specify a license.

If you plan to make the project open source, consider adding a suitable license such as the MIT License.

---

## 👩‍💻 Author

**Gayatri Tonde**

GitHub: `gayatri-tonde`

---

## ⭐ Support

If you find AutoSched useful, consider giving the repository a ⭐ on GitHub.

Contributions, suggestions, and feedback are welcome!
