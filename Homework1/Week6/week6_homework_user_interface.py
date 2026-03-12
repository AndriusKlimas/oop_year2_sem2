from week6_homework_class import Student


student_dict = {}

NotRunning = False

while not NotRunning:
    filename = input("Enter the filename: ")
    try:
        with open(f"{filename}.txt") as f:
            for line in f:
                line = line.strip()
                component = line.split(",")
                # 0 = id, 1 = name, 2 = subject, 3 = grade

                # looks if it has all 4 pieces of data
                if len(component) != 4:
                    print(f"Invalid line format (missing data): {line}")
                    continue

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

            # Successfully read the file, exit the loop
            NotRunning = True

    except FileNotFoundError:
        print("File not found. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
        NotRunning = True




print(student_dict)
