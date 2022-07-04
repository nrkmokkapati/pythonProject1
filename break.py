# how to break a loop
while True:
    s=input('Enter a string: ')
    if s=='quit':
        print('user entered quit and while loop is done')
        break
    else:
        print('length of string is ',len(s))

print('program completed')
