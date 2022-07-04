name='Ravi'
age=22
# usage of format strings
print('{0} was 22 years old when he came to US'.format(name))
print('{0} came to usa to study MS when he was {1} years old'.format(name, age))

# you can name the vars used in format strings
print('{name} was 22 years old when he came to US'.format(name=name))
print('{name} came to usa to study MS when he was {age} years old'.format(name=name, age=age))



#f strings will simplify the statements on how they look
print(f'{name} is a young man')
print(f'{name} was {age} years old when he came to US')


#input values in the format functon itself
print('{name} came on {flight} airlines when he came to USA'.format(name='Ravi', flight='delta'))