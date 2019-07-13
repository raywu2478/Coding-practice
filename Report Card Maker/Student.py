class Student:

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.test_results = {}
        self.courses = {}

    def say(self):
        print("id: ", self.student_id)
        print("name: ", self.name)
        print("test_results: ", self.test_results)
        print("courses: ", self.courses)
