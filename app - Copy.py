from flask import Flask, render_template, request
from generator import generate_all_timetables

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/generate', methods=['POST'])
def generate():
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    num_periods = int(request.form['num_periods'])
    num_breaks = int(request.form['num_breaks'])
    classrooms = int(request.form['classrooms'])
    sections = int(request.form['sections'])
    working_days = request.form['working_days'].split(',')
    break_durations = [int(d) for d in request.form['break_durations'].split(',') if d.strip().isdigit()]

    subjects = []
    i = 1
    while f"subject_name_{i}" in request.form:
        name = request.form[f"subject_name_{i}"]
        freq = int(request.form[f"subject_freq_{i}"])
        dur = int(request.form[f"subject_dur_{i}"])
        faculty = request.form[f"subject_faculty_{i}"]
        subjects.append({'name': name, 'freq': freq, 'dur': dur, 'faculty': faculty})
        i += 1

    timetables = generate_all_timetables(start_time, end_time, num_periods, num_breaks, break_durations,
                                         classrooms, sections, working_days, subjects)

    return render_template('timetable.html', timetables=timetables, working_days=working_days)

if __name__ == '__main__':
    app.run(debug=True)