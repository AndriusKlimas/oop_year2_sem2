from types import NotImplementedType


class InvalidIDError(Exception):
    pass

class InvalidGradeError(ValueError):
    pass


class Student():

    __id_prefix = "D0"


    def __init__(self, student_id:str, name:str, subject_grade:dict):
        '''Creats an instance of student containing a specific value.
        if value does not meet requirements, then error is raised

        Args:
            student_id (str): the id of the student
            name (str): the name of the student
            subject_grade (dict): the subject grade
        '''

        #Student id must start with a specific begining
        valid, error_msg = Student.validate_id(student_id)
        if valid:
            self._student_id = student_id
        else:
            raise InvalidIDError(error_msg)

        # Grade must be a valid number
        # valid, error_msg = Student.validate_grade(grade)
        # if valid:
        #     self._grade = grade
        # else:
        #     raise InvalidGradeError(error_msg)

        # NO logic for name structure - no validation needed
        self._name = name
        self._subject_grade = subject_grade

        # # No logic for subject structure - no validation needed
        # self._subject = subject



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

    # def get_subject(self) -> str:
    #     '''
    #     Returns the subject of the student
    #     return:
    #     Returns the current subject(as its stored)
    #     '''
    #
    #     return self._subject

    # def get_grade(self) -> float:
    #     '''
    #     Returns the grade of the student
    #
    #     return:
    #     Returns the current grade(as its stored)
    #     '''
    #     return self._grade

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
        return self._student_id >= other._student_id


    def __str__(self):
        '''
        Returns the string representation of the student
        return:
         a text representation of the student object
        '''
        return f"{self.get_student_id()} {self.get_name()}{self._subject_grade} "

    def __repr__(self):
        '''
        returns a developer friendly string representation of the student
        return:
        a texted string representation of the student object
        '''

        return (f"{self.__class__.__name__}{{_student_id={self._student_id},name={self.get_name()},{self._subject_grade}")



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
    def validate_grade(grade) -> tuple[bool, str] | tuple[bool, None]:
        if grade is None:
            return False, "Grade cannot be None"

        try:
            grade = float(grade)
        except (ValueError, TypeError):
            return False, "Grade must be an integer or float"

        if grade < 0 or grade > 100:
            return False, "Grade must be between 0 and 100"


        return True, None


    @staticmethod
    def add_grade(subject:str, grade:float, student_dict: dict) -> tuple[bool, str] | tuple[bool, None]:
        # Validate the grade first
        valid, error_msg = Student.validate_grade(grade)
        if not valid:
            return False, error_msg

        # Check if subject already exists in the dictionary
        if subject in student_dict:
            return False, "Grade already exists for this subject: " + subject

        # Add the grade for this subject
        student_dict[subject] = grade
        return True, None

