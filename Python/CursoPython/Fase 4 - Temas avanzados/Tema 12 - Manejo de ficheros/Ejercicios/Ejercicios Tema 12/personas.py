from io import open

file = open('personas.txt', 'r', encoding="utf8")

lines = file.readlines()

file.close()

persons = []

for line in lines:
	fields = line.split(';')
	person = {'id':fields[0], 'name':fields[1], 'surname':fields[2], 'birthdate':fields[3]}
	persons.append(person)


for person in persons:
	print('ID: {}  Name: {}  Surname: {}  Birthdate: {}'.format(person['id'], person['name'], person['surname'], person['birthdate']))



