def spam(divide_by):
    try:
        return 42 / divide_by
    except:
        print('Error, invalid argument')

print(spam(2))
print(spam(10))
print(spam(0))
print(spam(1))