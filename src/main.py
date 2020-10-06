import json


class Persons():
    def __init__(self, path):
        config = json.loads(open(path).read())
        self.name = config['name']
        self.age = config['age']
        self.gender = config['gender']

    def greet(self):
        message = f'Hello, my name is {self.name}.'
        return message


class Students(Persons):
    def learn(self, subject_name):
        message = f'I learn {subject_name} here.'
        return message


class Tutors(Persons):
    def teach(self, subject_name):
        message = f'I teach {subject_name} here.'
        return message


student = Students('../configs/student.json')
tutor = Tutors('../configs/tutor.json')

print(student.greet())
print(student.learn('Math'))

print(tutor.greet())
print(tutor.teach('History'))
