print('Hello World')
print('What is your name?') # asks for their name
my_name = input()
print('It is good to meet you, ' + my_name)
print('The length of your name is ' + str(len(my_name)))
print('What is your age?') # asks for their age
my_age = input()
print('You\'ll be ' + str(int(my_age) + 1) + ' in a year!')
if my_name == 'Munir':
    print('Here it is! The creator!')
if int(my_age) == 22:
    print('Crazy number, eh?')
elif int(my_age) < 12:
    print('Too young...')
elif int(my_age) > 30:
    print('Ewww, to old!')
else:
    print('You\'re not Munir!')

while my_name != 'Munir':
    print('Hey! I don\'t know that name! Try again...')
    my_name = input()
print('Thank you!')

total = 0
for num in range(101):
    total += num
print(total)