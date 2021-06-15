#2a
student_scores = {
    "Amy" : 67,
    "Billy" : 70,
    "Charlie" : 90,
    "Daisy" : 75,
    "Emily" : 71
}

print(student_scores)

#2b

def addKeyValue(key, value):
    print(f'added key is {key} and added value is {value}')
    student_scores.update({key : value})

addKeyValue("Fan", 85)

print(student_scores)

#2c

passStudents = {}

passStudents = {k : v for k, v in student_scores.items() if v >= 70 }



print(passStudents)