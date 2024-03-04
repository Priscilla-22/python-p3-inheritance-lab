#!/usr/bin/env python

from user import User


class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, added_knowledge):
        return self.knowledge.append(added_knowledge)


student = Student('Ann', 'Maria')
student.learn("hjakhdkjhasjshj")
print(student.knowledge)