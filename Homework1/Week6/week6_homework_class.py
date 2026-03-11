from types import NotImplementedType


class Student():

    __id_prefix = "D00"

    student_dict = {}

    def __init__(self, student_id:str, name:str, subject:str, grade:int):
        '''Creats an instance of student containing a specific value.
        if value does not meet requirements, then error is raised

        Args:
            student_id (str): the id of the student
            name (str): the name of the student
            subject (str): the subject of the student
            grade (int): the grade of the student
        '''

        #Student id must start with a specific begining
        valid, error_msg = Student.validate_id(student_id)
        if valid:
            self.student_id = student_id
        else:
            raise Exception(error_msg)

        #Grade must be a valid number
        valid, error_msg = Student.validate_grade(grade)
        if valid:
            self._grade = grade
        else:
            raise Exception(error_msg)

        # NO logic for name structure - no validation needed
        self._name = name

        # No logic for subject structure - no validation needed
        self._subject = subject



    #Returning the iteams so that they can be used

    def get_student_id(self) -> str:
        ''' Returns the id of the student

        return:
            Returns the current student id(as its stored)
        '''

        return self._student_id

    def get_name(self) -> str:
        '''
        Returns the name of the student

        return:
        Returns the current student name(as its stored)
        '''
        return self._name

    def get_subject(self) -> str:
        '''
        Returns the subject of the student
        return:
        Returns the current subject(as its stored)
        '''

        return self._subject

    def get_grade(self) -> int:
        '''
        Returns the grade of the student

        return:
        Returns the current grade(as its stored)
        '''
        return self._grade

    @staticmethod
    def get_prefix() -> str:
        '''
        Returns the prefix for the student id
        return:
        the required prefix to be present at the start of student id
        '''
        return Student.__id_prefix

    #Good Practice

    def __eq__(self, other) -> NotImplementedType:
        """Check if this _student_id is equil.
        (Student _student_id is the identifying attribute of a Student object)

        Args:
            other: The Student to compare this Student to

        Returns:
            True if the _student_id values are equal, False otherwise.
            If the parameter is not a _student_id, returns NotImplemented.
        """
        if not isinstance(other, Student):
            return NotImplemented
        return self._student_id == other._student_id


    def __ne__(self, other) -> NotImplementedType:
        """Check if this _student_id is not equil.
        (Student _student_id is the identifying attribute of a Student object)

        Args:
            other: The Student to compare this Student to

        Returns:
            True if the _student_id values are not equal, False otherwise.
            If the parameter is not a _student_id, returns NotImplemented.
        """


        if not isinstance(other, Student):
            return NotImplemented
        return not self._student_id == other._student_id

    def __hash__(self) -> int:
        return hash(self._student_id)

    def __lt__(self, other) -> NotImplementedType:
        if not isinstance(other, Student):
            return NotImplemented
        return self._student_id < other._student_id

    def __le__(self, other) -> NotImplementedType:
        if not isinstance(other, Student):
            return NotImplemented
        return self._student_id <= other._student_id

    def __gt__(self, other) -> NotImplementedType:
        if not isinstance(other, Student):
            return NotImplemented
        return self._student_id > other._student_id

    def __ge__(self, other) -> NotImplementedType:
        if not isinstance(other, Student):
            return NotImplemented
        return self._grade >= other._grade



    #Validation

    @staticmethod
    def validate_id(student_id:str) -> tuple[bool, str] | tuple[bool, None]:
        #Checking if None
        if student_id is None:
            return False, "Student ID cannot be None"
        #Checking if it starts with prefix
        if not student_id.startswith(Student.__id_prefix):
            return False, "Student ID must start with " + Student.__id_prefix
        #if both pass
        return True, None


    @staticmethod
    def validate_grade(grade:int) -> tuple[bool, str] | tuple[bool, None]:
        if grade is None:
            return False, "Grade cannot be None"

        if grade < 0 or grade > 100:
            return False, "Grade must be between 0 and 100"

        if not grade.isdigit():
            return False, "Grade must be an integer or float"

        return True, None


    @staticmethod
    def add_grade(subject:str, grade:int, student_dict: dict) -> Student:
        grade = Student.validate_grade(grade)

        for key, value in student_dict.values():
            if subject != key:
                student_dict[subject] = grade
                return True, None


            else:
                return False, "Grade already exists, for this subject " + {subject}

