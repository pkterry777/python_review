na = input()
ge = input()
g1 = eval(input())
g2 = eval(input())
g3 = eval(input())
lst = [g1,g2,g3]

class student:
    def __init__(self,name,gender):
        self.name = na
        self.gender = ge
        self.grades = []
    def avg():
        return sum(student.grades)/len(student.grades)
    def add (student,score):
        student.grades.append(score)
    def fcount(self):
        fct = 0
        for i in range(len(student.grades)):
            if student.grades < 0:
                fct += 1
            print(fct)

x = student(na,ge)
print(x.name)
print(x.avg())
print(x.fcount())
