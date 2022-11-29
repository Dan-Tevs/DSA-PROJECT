import random



def guess_num():
    flag = True
    while flag:
        num = input('Type a number for an upper bound: ')

        if num.isdigit():
            print("Let's Play!")
            num = int(num)
            flag = False
        else:
            print('Invalid Input! Try Again!')

    secret = random.randint(1,num)

    guess = None
    count = 1

    while guess != secret:
        guess = input('Type a number between 1 and ' + str(num) + ': ')
        if guess.isdigit():
            guess = int(guess)

        if guess == secret:
            print('Congratulations! You got it!')
        else:
            print('Incorrect, Please try again!')
            count += 1
    print('It took you', count, 'guesses!')
    
guess_num()


