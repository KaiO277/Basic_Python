# students = {
#     "Nghia Tran" : "QN",
#     "KaiO" : "DN",
#     "Lorem" : "HN",
# }

# for student in students :
#     print(student, students[student], sep=", ")

students = [
    {"name": "Nghia", "house": "QN", "class": "U"},
    {"name": "KaiO", "house":"DN", "class": "U"},
    {"name": "KO", "house":"HN", "class":"1"},
    {"name":"KKOO", "house":"HCM", "class":None}
]

for student in students:
    print(student["name"], student["house"], student["class"], sep=", ")