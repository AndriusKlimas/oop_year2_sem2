from week6_homework_class import Student

filename = input("Enter the filename: ")
student_dict = {}


with open(f"{filename}.txt") as f:
    for line in f:
        line = line.strip()
        component = line.split(",")
        # 0 = id, 1 = name, 2 = subject, 3 = grade

        student_id = component[0]
        name = component[1]
        subject = component[2]

        # Validate student ID
        valid, error_msg = Student.validate_id(student_id)
        if not valid:
            print(error_msg)
            continue

        # Validate grade
        valid, error_msg = Student.validate_grade(component[3])
        if not valid:
            print(error_msg)
            continue

        grade = float(component[3])

        # Check if student already exists
        if student_id in student_dict:
            # Student exists, add the new subject/grade to their dict
            existing_student = student_dict[student_id]
            valid, error_msg = Student.add_grade(subject, grade, existing_student._subject_grade)
            if not valid:
                print(error_msg)
                continue
        else:
            # New student, create a subject_grade dictionary
            subject_grade = {}
            valid, error_msg = Student.add_grade(subject, grade, subject_grade)
            if not valid:
                print(error_msg)
                continue

            # Create new student
            student = Student(student_id, name, subject_grade)
            student_dict[student_id] = student



print(student_dict)
