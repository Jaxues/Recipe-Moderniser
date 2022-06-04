#First Version if recipe moderniser
#Get user unit from user to convert to grams or millitres
i=1
#i created for while loops.
#Tuple of suitable units for both grams and mills
unit_to_grams=('ounce',
                   'pound',
                   'stick',
               'onces',
               'pounds',
               'sticks')
units_to_mills=('teaspoon',
                    'tablespoon',
                    'cup',
                    'quart',
                    'pint',
                'teaspoons',
                'tablespoons',
                'cups',
                'pints')
while i>0:
    while i ==1:
        user_measure=input('Please enter a unit you would like to convert? ')
        #Get the number of units they want to convert
        if user_measure.lower() in unit_to_grams:
            print('The program will now convert {} to grams.'.format(user_measure.lower()))
            break
        elif user_measure.lower() in units_to_mills:
            print('The program will now convert {} to milliliters'.format(user_measure.lower()))
            break
        else:
            print('Please enter a valid response.')
    user_number_measures=int(input('Please enter the number of {}s you would like to convert? '.format(user_measure)))
    #Confirmation
    confirmation_message=input('Did you want to convert {} {}? '.format(user_number_measures,user_measure))
    if confirmation_message.lower() == 'yes':
        print('Great the program will convert {} {} now.'.format(user_number_measures,user_measure))
        break
    elif confirmation_message.lower() == 'no':
        print('Please enter the number of units you would like to convert.')
    else:
        print('Please enter a valid response.')
