x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#ex1
x[1][0]=15 

for student in students:
    if student['last_name'] == 'Jordan':
        student['last_name'] = 'Bryant'

print(students)

sports_directory['soccer'][sports_directory['soccer'].index('Messi')] = 'Andres'

print(sports_directory)