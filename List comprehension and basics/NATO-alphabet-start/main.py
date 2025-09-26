student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
#data_dict={new_key:new_value for (index,row) in dataframe.iterrows()}
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
letter=[]
code=[]
nato_phonetic=pandas.read_csv("nato_phonetic_alphabet.csv") 
# nato=nato_phonetic.to_dict()  this will convert out the data in format of {'letter': {0: 'A', 1: 'B', 2: [each column has it's own sepearte dict with index sepaarte key and separte value.]

data_dict={row.letter:row.code for (index,row) in nato_phonetic.iterrows()}  #{"A": "Alfa", "B": "Bravo"} this will give us the desired result liek this looping through each index row one by one and fetching row . letter and code as new key and value

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_on=True
while is_on:
    user_name=input("Enter your name: ").upper()
    try: 
        user_code=[data_dict[letter] for letter in user_name]
    except KeyError:
        print("Sorry only letters in alphabets please.")
    else:
        print("HERE IS YOUR PHONETIC MESSAGE.\n")
        print(user_code)
    finally:
        user_choice=input("Do you want another phonetic message? 'y' or 'n' :")
        if user_choice=='n':
            is_on=False
            print("See you next time.")

