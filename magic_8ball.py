import random

def get_answer(answer_number):
    switcher = {
        1: 'It is certain',
        2: 'It is decidely so',
        3: 'Yes',
        4: 'Reply hazy try again',
        5: 'Ask again later',
        6: 'Concentrate and ask again',
        7: 'My reply is no',
        8: 'Outlook not so good',
        9: 'Very doubtful'
    }
    return switcher.get(answer_number)

r = random.randint(1, 9)
fortune = get_answer(r)
print(fortune)