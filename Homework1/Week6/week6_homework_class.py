from types import NotImplementedType


class Student():

    __id_prefix = "D00"

    def __init__(self, student_id:str, name:str, subject:str, grade:int):
        self._student_id = student_id
        self._name = name
        self._subject = subject
        self._grade = grade


    #Returning the iteams so that they can be used

    def get_student_id(self) -> str:
        return self._student_id

    def get_name(self) -> str:
        return self._name

    def get_subject(self) -> str:
        return self._subject

    def get_grade(self) -> int:
        return self._grade

    @staticmethod
    def get_prefix() -> str:
        return Student.id_prefix

    #Good Practice

    def __eq__(self, other) -> NotImplementedType:
        if not isinstance(other, Student):
            return NotImplemented
        return self._grade == other._grade


    def __ne__(self, other) -> NotImplementedType:
        if not isinstance(other, Student):
            return NotImplemented
        return not self == other

    def __hash__(self) -> int:
        return hash(self._grade)

    def __lt__(self, other) -> NotImplementedType:
        if not isinstance(other, Student):
            return NotImplemented
        return self._grade < other._grade

    def __le__(self, other) -> NotImplementedType:
        if not isinstance(other, Student):
            return NotImplemented
        return self._grade <= other._grade

    def __gt__(self, other) -> NotImplementedType:
        if not isinstance(other, Student):
            return NotImplemented
        return self._grade > other._grade

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




