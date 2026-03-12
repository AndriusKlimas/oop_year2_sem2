from week6_homework_class import Student


student_dict = {}


def pulling_file():
    not_running = False
    while not not_running:
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
                print(f"\nSuccessfully loaded {len(student_dict)} student(s).")
                not_running = True

        except FileNotFoundError:
            print("File not found. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
            not_running = True


def find_user():
    name_id = input("Enter the student name: ").lower()
    found = False
    #For the students name and id
    for student_id, student in student_dict.items():
        if student.get_name().lower() == name_id:
            print(f"Student found!")
            print(f"ID: {student.get_student_id()}, Name: {student.get_name()}")
            print(f"Subjects and Grades:")
            #Need to search throught the subject_grades dict to get them sepretly, cause i have no clue how to do it
            # any other way
            for subject, grade in student._subject_grade.items():
                print(f"  - {subject}: {grade}")
            found = True
            break

    if not found:
        print("Student not found.")




if __name__ == "__main__":
    keepgoing = True
    while keepgoing:
        want = input("\nPlease enter what you would like to do:\n 1. pull file\n 2. search for student\n 3. quit\n> ")

        match want:
            case "1":
                pulling_file()
            case "2":
                find_user()
            case "3":
                print("Goodbye!")
                keepgoing = False
            case _:
                print("Invalid option. Please choose 1, 2, or 3.")


