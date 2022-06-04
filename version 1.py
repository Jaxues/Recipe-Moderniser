#First Version if recipe moderniser
#Get user unit from user to convert to grams or millitres
user_measure=input('Please enter a unit you would like to convert? ')
#Get the number of units they want to convert
user_number_measures=int(input('Please enter the number of {}s you would like to convert? '.format(user_measure)))
#Confirmation
confirmation_message=input('Did you want to convert {} {}s? '.format(user_number_measures,user_measure))
if confirmation_message.lower() == 'yes':
    print('Great the program will convert {} {} now.'.format(user_number_measures,user_measure))
elif confirmation_message.lower() == 'no':
    print('Please enter the number of units you would like to convert.')
else:
    print('Please enter a valid response.')
