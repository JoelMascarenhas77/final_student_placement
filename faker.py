import csv
from faker import Faker
import random
import roman

fake = Faker()
num_students = 5

student_data = []

for _ in range(num_students):
    first_name = fake.first_name()
    student = {
        'pid': fake.unique.random_int(min=1000, max=9999, step=1),
        'first_name': first_name,
        'last_name': fake.last_name(),
        'age': random.randint(18, 30),
        'gender': random.choice(['Male', 'Female']),
        'hostel': random.choice(['Yes', 'No']),
        'address': fake.address(),
        'branch': fake.word(ext_word_list=['Computer Science', 'Electrical', 'Information Technology', 'Civil', 'Electronics & Communication', 'Mechanical']),
        'semester': roman.toRoman(random.randint(1, 8)),
        'division': random.choice(['A', 'B']),
        'username': first_name[:4].lower(),
        'password': '12345678',
        'email': fake.unique.email(),
    }
    student_data.append(student)

# Define the CSV file name
csv_file = 'fake_students.csv'

# Write the student data to a CSV file
with open(csv_file, mode='w', newline='') as file:
    fieldnames = student_data[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for student in student_data:
        writer.writerow(student)

print(f'{num_students} fake student records have been saved to {csv_file}')
