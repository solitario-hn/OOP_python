#TODO 1: Writing a list comprehension to square each number in list
#[new_item for new_item in items if test]
list=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers=[n*n for n in list]       #[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]

#TODO 2: Converting strings into int from a list and then, finding out even numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers=[int(n) for n in list_of_strings]
result=[num for num in numbers if num%2==0]   #[0, 32, 8, 2, 8, 64, 42]

#TODO 3:LEARNING DICTIONARY COMPREHENSION
#new_dict={new_key:new_value for item in list}
#new_dict={new_key:new_value for (key,value) in dict.items() if test}     #from an exisiting dictionary.
import random
names=["Nisha","Mehak","Niharika","Huma","Karishma","Katrina","Kareena"]
student_scores={student:random.randint(1,100) for student in names}    #{'Nisha': 89, 'Mehak': 80, 'Niharika': 54, 'Huma': 65, 'Karishma': 38, 'Katrina': 25, 'Kareena': 51}
passed_students={student:score for (student,score) in student_scores.items() if score>=60}

#TODO 4:  
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result={word:len(word) for word in sentence.split()}  #split functions splits the sentence into separate words in this case separated by a space you can also use an argument separator.()

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f={Day:(temp * 9/5) + 32 for (Day,temp) in weather_c.items()}
# for (index,row) in student_dataframe.iterrrows():
#     print(index)   prints index value
#     print(row)      prints each row in dataframe format
#     print(row.score)   prints score of each row.

