my_pets = ['Goiabada', 'Angel', 'Kitty', 'Guida']

print('Enter a pet name:')
name = input('> ')

if name not in my_pets:
    print('I don\'t have a pet named ' + name)
else:
    print(name + ' is my pet')