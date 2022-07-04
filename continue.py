#continue to let the rest of the statemets process by skipping
while True:
    s=input('Enter a string: ')
    if s=='quit':
        print('user entered quit and while loop is breaken now')
        break
    if len(s)<5:
        print('String is small')
        continue
        print('ravi') #this line is skipped if string is of sufficient lenght
    print('Input is of sufficient length')
    print('Success- you have entered a string of sufficient length')
print('Programm is done')