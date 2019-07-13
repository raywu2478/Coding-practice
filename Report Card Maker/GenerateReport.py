import csv
import sys
from Student import Student
from Course import Course

student_list = []
course_list = []


def student_get_grade(c):
    for s in student_list:
        if set(c.tests) & (set(s.test_results)) == set(c.tests):
            s.courses[c.course_id] = \
                sum(list(map(lambda k: int(s.test_results.get(k))*int(c.tests.get(k))/100, c.tests.keys())))
        elif set(c.tests) & (set(s.test_results)) == set():
            continue
        else:  # if intersection is not itself or null set, then course information is incomplete
            print("Error when processing student id: ", s.student_id)
            sys.exit("Student has incomplete mark info")


def course_get_info(k):
    tmp = next(c for c in course_list if c.course_id == k)
    return tmp.name, tmp.teacher


def generate_report(s):
    report = open("report.txt", "a")
    report.write("Student Id: {}, name: {}\n".format(s.student_id, s.name))
    report.write("Total Average:\t\t{:.2f}\n".format(sum(s.courses.values())/len(s.courses)))
    for k in sorted(s.courses.keys()):
        report.write("\n\tCourse: {}, Teacher: {}\n\tFinal grade:\t{:.2f}\n".format(*course_get_info(k), s.courses.get(k)))
    report.write("\n\n\n")
    report.close()


# read inputs from file
with open('students.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # skip header
    next(csv_reader, None)
    for row in csv_reader:
        # generate list of student objects
        student_list.append(Student(row[0], row[1]))

with open('marks.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)
    for row in csv_reader:
        # filter object in list by student_id
        next(s for s in student_list if s.student_id == row[1]).test_results[row[0]] = row[2]

with open('courses.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)
    for row in csv_reader:
        # generate list of course objects
        course_list.append(Course(row[0], row[1], row[2]))

with open('tests.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)
    for row in csv_reader:
        # filter object in list by course_id
        next(c for c in course_list if c.course_id == row[1]).tests[row[0]] = row[2]

list(map(student_get_grade, course_list))

list(map(generate_report, sorted(student_list, key=lambda x: x.student_id)))
