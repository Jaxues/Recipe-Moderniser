#This is the fourth version of the recipe moderniser 
#Get user unit from user to convert to grams or millitres
i=1
#i created for while loops.
#Tuple of suitable units for both grams and mills
#List for all values
measures=[]
numbers=[]
conversions={}
#List of all units for grams and mills
unit_to_grams=('ounce','pound','stick')
unit_to_mills=('teaspoon','tablespoon','cup','quart','pint')
#List of all  abbreviations
abbreviations_grams=('oz','lb','stk')
abbreviations_mills=('tsp','tbs','tbsp','c','qt','pt')
#Dictionary of abbreviations
abbreviations_convert_grams={'oz':'ounce',
                   'lb':'pound',
                   'stk':'stick'}
abbreviations_convert_mills={'tsp':'teaspoon',
                   'tbs':'tablespoon',
                   'tbsp':'tablespoon',
                   'c':'cup',
                   'qt':'quart',
                   'pt':'pint'}
#Lost of all plurals
plural_grams=('ounces','pounds','sticks')
plural_mills=('teaspoons','tablespoons','cups','quarts','pints')
#Dictionary of plurals
plural_convert_grams={'ounces':'ounce',
              'pounds':'pound',
              'sticks':'stick'}
plural_convert_mills={'teaspoons':'teaspoon',
              'tablespoons':'tablespoon',
              'cups':'cup',
              'quarts':'quart',
              'pints':'pint'}
    
#Conversion from units to grams
conversion_to_grams = {'ounce':28.35,
                      'pound':454,
                      'stick':113}
#Have set conversion for measures to grams so that can be used to retrieve later
conversion_to_mills = {'cup':240,'cups':240,
                    'american cup':250,
                      'teaspoon':5,
                      'tablespoon':15,
                       'pint':473,
                       'quart':946}
#Gather user input
while i ==1:
    user_measure=input('Please enter a unit you would like to convert? ')
    #Determines whether measure is to be convert to grams.
    if user_measure.lower() in abbreviations_grams:
            user_measure=abbreviations_convert_grams[user_measure]
            print("Great the program will now convert {}s to grams.".format(user_measure.lower()))
            measures.append(user_measure)
            #Convert user measure which is abbreviation to corrosponding unit and add unit to list for conversion
            if user_measure.lower() == 'cup':
                while i>0:
                    is_american_cup=input("Is the recipe american? ")
                    if is_american_cup.lower() == 'yes':
                       user_measure="american cup"
                    elif is_american_cup.lower()=='no':
                        break
                    else:
                        print('Please enter a valid response')
    elif user_measure.lower() in plural_grams:
        user_measure=plural_convert_grams[user_measure]
        measures.append(user_measure)
        print("Great the program will now convert {}s to grams.".format(user_measure.lower()))
        measures.append(user_measure)
        #Convert user measurement which is plural to corrosponding unit and add unit to list for conversion
        if user_measure.lower() == 'cup':
            while i>0:
                    is_american_cup=input("Is the recipe american? ")
                    if is_american_cup.lower() == 'yes':
                       user_measure="american cup"
                    elif is_american_cup.lower()=='no':
                        break
                    else:
                        print('Please enter a valid response')
    elif user_measure in unit_to_grams: 
        print("Great the program will now convert {}s to grams.".format(user_measure.lower()))
        measures.append(user_measure)
        #Will print message telling that measurement user enter will be convertered to grams. 
        if user_measure.lower() == 'cup':
            while i>0:
                    is_american_cup=input("Is the recipe american? ")
                    if is_american_cup.lower() == 'yes':
                       user_measure="american cup"
                    elif is_american_cup.lower()=='no':
                        break
                    else:
                        print('Please enter a valid response')    
    #Determines whether measure is to be convert to mills. 
    elif user_measure.lower() in abbreviations_mills:
        user_measure=abbreviations_convert_mills[user_measure]
        print("Great the program will now convert {}s to mills.".format(user_measure.lower()))
        measures.append(user_measure)
        #Convert user measure which is abbreviation to corrosponding unit and add unit to list for conversion
    elif user_measure.lower() in plural_mills:
        user_measure=plural_convert_mills[user_measure]
        print(user_measure)
        print("Great the program will convert {}s to grams".format(user_measure))
        #Convert user measurement which is plural to corrosponding unit and add unit to list for conversion
    elif user_measure.lower() in unit_to_mills: 
        print("Great the program will now convert {}s to mills.".format(user_measure.lower()))
        measures.append(user_measure)
        #Will print message telling that measurement user enter will be convertered to mills and add to list of measurements.        
    #If not other two then must not be valid response so will print message to user to enter a valid response. 
    else:
        print("Please eneter a valid response.")
    user_number_measures=int(input('Please enter the number of {}s you would like to convert? '.format(user_measure.lower())))
    numbers.append(user_number_measures)
    #Confirmation
    user_confirmation=input("Did you want to convert {} {}?".format(user_number_measures,user_measure))
    while i >0:
        if user_confirmation.lower()=='yes':
            break
        elif user_confirmation.lower()=='no':
            print("Please enter units you would like to convert")
            continue
        else:
            print("Please enter a valid response.")
    
    continue_loop=input("Did you want to convert any more measurements?")
    if continue_loop.lower()=='yes':
        continue
    elif continue_loop.lower()=='no':
        break 
    else:
        print("Please Enter a valid response")
        continue
#Convert List of measure and number from what user has enetered. 
for (measure,number) in zip(measures,numbers):
        if measure in conversion_to_mills:
            final_conversion_mills=conversion_to_mills[measure.lower()]*number
            print("{} {}s is {} millitres".format(number,measure,final_conversion_mills))
        elif user_measure in conversion_to_grams:
            final_conversion_grams=conversion_to_grams[measure.lower()]*number
            print("{} {}s is {} grams".format(number,measure,final_conversion_grams))