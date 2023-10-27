import random
n = random.randint(1,100)
win = False
c = 0
m = ''
while not win:
    c += 1
    g = int(input(f'{m}guess time : {c} enter number 1-100 '))
    print(f'{c} : {g} => ', end = '')
    if g > n:
        m = f'less than {g} '
    elif g < n:
        m = f'more than {g} '
    elif g == n:
        m = f'{g} is correct'
        win = True
    print(f'{m}')
    if (not win) and (c == 7):
        print(f'you complete {c} guesses ')
        print(f'you lose the answer is {n}')
        break
if win == True:
    print('you win')