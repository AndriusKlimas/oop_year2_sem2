from types import NotImplementedType


class Student():
    def __init__(self, student_id:str, name:str, subject:str, grade:int):
        self._student_id = student_id
        self._name = name
        self._subject = subject
        self._grade = grade


    #Returning the iteams so that they can be used

    def get_student_id(self):
        return self._student_id

    def get_name(self):
        return self._name

    def get_subject(self):
        return self._subject

    def get_grade(self):
        return self._grade


