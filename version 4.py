#This is the fourth version of the recipe moderniser 
#Get user unit from user to convert to grams or millitres
i=1
#i created for while loops.
#Tuple of suitable units for both grams and mills
#List for all values
measures=[]
numbers=[]


#List of all units for grams and mills
unit_to_grams=('ounce','pound','stick')
unit_to_mills=('teaspoon','tablespoon','cup','quart','pint')
#Dictionary of abbreviations
abbreviations_grams={'oz':'ounce',
                   'lb':'pound',
                   'stk':'stick'}
abbreviations_mills={'tsp':'teaspoon',
                   'tbs':'tablespoon',
                   'tbsp':'tablespoon',
                   'c':'cup',
                   'qt':'quart',
                   'pt':'pint'}
#Dictionary of plurals
plural_grams={'ounces':'ounce','pounds':'pound','sticks':'stick'}
plural_mills={'teaspoons':'teaspoon','tablespoons':'tablespoon','cups':'cup','quarts':'quart','pints':'pint'}
#Function to convert abbreviations to units
def abbreviations(value):
    if value in abbreviations_grams:
        return abbreviations_grams[vlaue]
    elif value in abbreviations_mills:
        return abbreviations_mills[value]
#Function to convert plurals
def plurals(value):
    if value in plural_grams:
        return plural_grams[value]
    elif value in plural_mills:
        return plural_mills[value]
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

while i>0:
    while i ==1:
        user_measure=input('Please enter a unit you would like to convert? ')
        if user_measure.lower()  in abbreviations_grams or abbreviations_mills:
            user_measure=str(abbreviations(user_measure.lower()))
        elif user_measure.lower() in plural_grams or plural_mills:
            user_measure=str(plurals(user_measure.lower()))
     #Get the number of units they want to convert
        if user_measure.lower() in unit_to_grams:
            print('The program will now convert {} to grams.'.format(user_measure.lower()))  
            break
        elif user_measure.lower() in unit_to_mills:
            if user_measure.lower() == 'cup':
                america_or_not=input('Is ther recipe american?')
                if america_or_not.lower()=='yes':
                    user_measure='american cup'
                    break
                elif america_or_not.lower()== 'no':
                    break
                else:
                    print("Please enter a valid response.")
            print('The program will now convert {}s to milliliters'.format(user_measure.lower()))
            break
        else:
            print('Please enter a valid response.')
    user_number_measures=int(input('Please enter the number of {}s you would like to convert? '.format(user_measure.lower())))
    #Confirmation
    confirmation_message=input('Did you want to convert {} {}s? '.format(user_number_measures,user_measure.lower()))
    if confirmation_message.lower() == 'yes':
        print('Great the program will convert {} {}s now.'.format(user_number_measures,user_measure.lower()))
        measures.append(user_measure)
        numbers.append(user_number_measures)
        while i >0:
            continue_loop=input('Would you like to convert any more measurements?')
            if continue_loop.lower() == 'yes':
                a=1
                break
            elif continue_loop.lower() == 'no':
                for (measure,number) in zip(measures,numbers):
                    if measure in conversion_to_mills:
                        final_conversion_mills=conversion_to_mills[measure.lower()]*number
                        print("{} {}s is {} millitres".format(number,measure,final_conversion_mills))
                    elif user_measure in conversion_to_grams:
                        final_conversion_grams=conversion_to_grams[measure.lower()]*number
                        print("{} {}s is {} grams".format(number,measure,final_conversion_grams))
                    quit
                    break
            else:
                print('Please enter a valid response')
        if a >0:
            a-=1
            continue
        elif a == 0:
            pass
    elif confirmation_message.lower() == 'no':
        print('Please enter the number of units you would like to convert.')
        break
    else:
        print('Please enter a valid response.')
    if continue_loop.lower=='no':
        break


        
        
    
