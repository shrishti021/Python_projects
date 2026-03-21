# Student Grade Analyzer

students = {
    "Rahul":   [85, 92, 78, 90, 88],
    "Priya":   [45, 52, 38, 60, 55],
    "Arjun":   [95, 98, 92, 97, 99],
    "Sneha":   [70, 68, 75, 72, 69],
    "Dev":     [30, 25, 40, 35, 28],
}

def analyze_grades(students):
    students_avg = {}
    all_marks = []

    #calculate avg marks
    for name,marks in students.items():
        avg = sum(marks) / len(marks)
        students_avg[name] = round(avg, 2)
        all_marks.extend(marks)

    top_student = max(students_avg, key=students_avg.get)
    bottom_student = min(students_avg, key=students_avg.get)

    at_risk = []
    for name in students_avg:
        if students_avg[name] < 50:
            at_risk.append(name)
        
    class_avg = sum(all_marks) / len(all_marks)

    return {
        "averages" : students_avg,
        "top"  : top_student,
        "bottom" : bottom_student,
        "at_risk" : at_risk,
        "class_avg" : round(class_avg,2)
    }

report = analyze_grades(students)
print(report)
