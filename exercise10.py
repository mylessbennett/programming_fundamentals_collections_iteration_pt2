students = {
    'cohort 1': 34,
    'cohort 2': 42,
    'cohort 3': 22
}
#---------------------------------------------------------------
def display_cohorts(cohort_list):
    for cohort, num in students.items():
        print("{}: {} students".format(cohort, num))
#---------------------------------------------------------------
students['cohort 4'] = 43
#---------------------------------------------------------------
print(students.keys())
#---------------------------------------------------------------
for cohort, num in students.items():
    num = num + (num*0.05)
    students[cohort] = num

print(students)
#---------------------------------------------------------------
students.pop('cohort 2')
print(students)
#---------------------------------------------------------------
total = 0
for cohort, num in students.items():
    total = total + num

print("Total students: {}".format(total))
