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
                'pints','tsp','tbs')
while i>0:
    while i ==1:
        user_measure=input('Please enter a unit you would like to convert? ')
        #Get the number of units they want to convert
        if user_measure in unit_to_grams:
            print('The program will now convert {} to grams.'.format(user_measure))
            
            break
        elif user_measure in units_to_mills:
            if user_measure.lower() == 'teaspoons':
                user_measure = 'teaspoon'
            elif user_measure.lower() == 'tablespoons':
                user_measure ='tablespoons'
            elif user_measure.lower() == 'cups':
                user_measure = 'cup'
            elif user_measure.lower() == 'pints':
                user_measure = 'pint'
            elif user_measure.lower() == 'tsp':
                user_measure = 'teaspoon'
            elif user_measure.lower() == 'tbs':
                user_measure = 'tablespoon'
            while i <2:
                if user_measure.lower() == 'cup':
                    america_or_not=input('Is ther recipe american?')
                    if america_or_not.lower()=='yes':
                        user_measure='american cup'
                        break
                    elif america_or_not.lower()== 'no':
                        break
                    else:
                        print("Please enter a valid response.")
            print('The program will now convert {}s to milliliters'.format(user_measure))
            break
        else:
            print('Please enter a valid response.')
    user_number_measures=int(input('Please enter the number of {}s you would like to convert? '.format(user_measure)))
    #Confirmation
    confirmation_message=input('Did you want to convert {} {}s? '.format(user_number_measures,user_measure))
    if confirmation_message.lower() == 'yes':
        print('Great the program will convert {} {}s now.'.format(user_number_measures,user_measure))
        break
    elif confirmation_message.lower() == 'no':
        print('Please enter the number of units you would like to convert.')
    else:
        print('Please enter a valid response.')
"""
Teaspoon (tsp)	5 mL
Tablespoon (tbs)	15 mL
Cup	240 mL (US) or 250 mL (NZ)
1 ounce	28.35 g
1 pint	473 mL
Quart	946 mL
Pound	454 g
Stick*	113 g
"""
#Conversion from units to grams
conversion_to_grams = {'ounce':28.35,
                      'pound':454,
                      'stick':113}
#Have set conversion for measures to grams so that can be used to retrieve later
conversion_to_mills = {'cup':240,
                       'cups':240,
                       'american cup':250,
                      'teaspoon':5,
                      'tablespoon':15,
                       'pint':473,
                       'quart':946}
if user_measure in conversion_to_mills:
    final_conversion_mills=conversion_to_mills[user_measure]*user_number_measures
    print("{} {}s is {} millitres".format(user_number_measures,user_measure,final_conversion_mills))
elif user_measure in conversion_to_grams:
    final_conversion_grams=conversion_to_grams[user_measure]*user_number_measures
    print("{} {}s is {} grams".format(user_number_measures,user_measurefinal_conversion_grams))
        
        
    
