class Course:

    def __init__(self, course_id, name, teacher):
        self.course_id = course_id
        self.name = name
        self.teacher = teacher
        self.tests = {}

    def say(self):
        print("id: ", self.course_id)
        print("name: ", self.name)
        print("teacher: ", self.teacher)
        print("tests: ", self.tests)

    def course_tests(self):
        return self.tests.keys()
