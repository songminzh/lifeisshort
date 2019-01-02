#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
    
    def print_score(self):
        print('Name:%s\nScore:%s' % (self.name, self.score))

bart = Student('Bart Simpson', 81)
bart.print_score()
print('Grade: %s' % bart.get_grade())