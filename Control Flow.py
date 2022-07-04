# if else condition
number=24
guess=int(input('Enter a number: '))
if guess==number:
    print('Congrats, you guessed the right number')
elif guess<number:
    print('Guessed number is lower than actual number')
else:
    print('Guessed number is greater than actual number')
print('Want to Try again?')

#while condition
number=23
running=True

while running:
    guess=int(input('Enter a number: '))
    if guess==number:
        print('Congrat\'s, you guessed the correct value')
        running=False
    elif guess<number:
        print('Guessed number is lower than actual value')
    else:
        print('Guessed number is greater than actual value')
else:
    print('While Loop is over')
print('Done')

#for loop
i=1
for i in range(1,5):
    #print(i,end=' ')
    print(i)
    i=i+1
else:
    print('for loop is done')



print(list(range(5)))
