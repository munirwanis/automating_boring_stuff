def collatz(number):
    value = 0
    if number % 2 == 0:
        value = number // 2
    else:
        value = 3 * number + 1
    print(value)
    return value

value = 0
print('Enter some number:')
while True:
    try:
        value = int(input())
        break
    except:
        print('Value not valid! Must be a number.')

while value != 1:
    value = collatz(value)