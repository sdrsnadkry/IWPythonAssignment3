import csv

csv_columns = ['Id', 'Course', 'Duration', 'Teacher']
dict_data = [
    {'Id': 1, 'Course': 'Python', 'Duration': '6 Weeks', 'Teacher': 'Mr.Hari'},
    {'Id': 2, 'Course': 'JavaScript', 'Duration': '6 Weeks', 'Teacher': 'Mr.Raju'},
    {'Id': 3, 'Course': 'React', 'Duration': '6 Weeks', 'Teacher': 'Mr.Shyam'},
    {'Id': 4, 'Course': 'Java', 'Duration': '6 Weeks', 'Teacher': 'Mr.Ram'},
    {'Id': 5, 'Course': 'Php', 'Duration': '6 Weeks', 'Teacher': 'Mr.Madan'},
]

with open("courses.csv", 'w') as course_csv:
    writer = csv.DictWriter(course_csv, fieldnames=csv_columns)
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)
