import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manataltest.settings')

import django
django.setup()    

from app.models import Student, School
from faker import Faker
from itertools import product
import random
from django.db.models import Count

def schoolFakeData():
    faker = Faker()
    fake_name = faker.name()[:3].upper()
    fake_addr = faker.address() 
    fake_max = random.randint(30,1000)

    # Generate fake data
    newSchool = School(schoolName= fake_name, schoolAddress= fake_addr, maxStudent= fake_max)
    newSchool.save()

def fakeSchoolId():
    # Count the amount of students in particular school
    studentCount = Student.objects.order_by('schoolId').values('schoolId').annotate(Count("schoolId"))
    avilableSchool = School.objects.order_by('id').all()

    # Filter only schools that have avialable seats
    filtered_schoolId = list()
    for school, student in zip(avilableSchool, studentCount):
        if school.maxStudent > student['schoolId__count']:
            filtered_schoolId.append(school.id)
            
    # Return randomly selected schoolId
    return random.choice(filtered_schoolId)

def studentFakeData():
    faker = Faker()
    fake_fname = faker.first_name()
    fake_lname = faker.last_name()
    fake_email = faker.email()
    fake_gender = random.choice(['M', 'F'])
    fake_dob = faker.date()
    fake_schoolId = fakeSchoolId()

    # Generate fake data
    newStudent = Student(firstName = fake_fname, 
                         lastName = fake_lname, 
                         email = fake_email,
                         gender = fake_gender,
                         dob = fake_dob,
                         schoolId = School.objects.get(id = fake_schoolId)
                        )
    newStudent.save()

def genData(n_school=10, n_student=10, genSchool=True, genStudent=True):
    # Generate school data
    if genSchool:
        for _ in range(n_school):
            schoolFakeData()

    # Generate student data
    if genStudent:
        for _ in range(n_student):
            studentFakeData()

def main():
    print("Generating Data...")
    genData(5, 5, genSchool=True, genStudent=True)
    print("Complete!")

if __name__ == '__main__':
    main()