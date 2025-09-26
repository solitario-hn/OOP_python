# with open("weather_data.csv") as f:
#     data=f.readlines()
#     print(data)
    
# import csv
# with open("weather_data.csv") as f:        #creates an object for the file.
#     data=csv.reader(f) #saves the content of file in object format using csv module.
#     temperatures=[]
    
#     for row in data: #prints out each row elements sepaarted in one list in separate strings.
#         if row[1]=='temp':
#             pass
#         else:
#             temp=int(row[1])
#             temperatures.append(temp)
            
#     print(temperatures)
        
# import pandas
# weather_data= pandas.read_csv("weather_data.csv")
# print(type(weather_data))              #datatype here is dataframe type which is quite similar to the spreadsheet format
# print(type(weather_data['temp']))      #datatype here is series type which is equivalent to a column series .
     
#TODO 1 :to get hold of temp in a list format and calculate its avergae.
# list=weather_data['temp'].to_list()
# avg=sum(list)/len(list)
# print(avg)
# print(weather_data['temp'].max())     #using a direct method series.mean from the panndas lib.
# print(weather_data.condition)        #this will print out the condition column because pandas actually save each column name as an attribute.

#TODO 2: Get row in a data

# print(weather_data[weather_data.day=='Monday'])
# print(weather_data[weather_data.temp==weather_data.temp.max()])
# tuesday=weather_data[weather_data.day=='Tuesday']
# tuesday_temp=tuesday.temp[1]
# F = 9/5*tuesday_temp+32
# print(F)
# print(tuesday.temp)           #this returns the temp in form of a sequence that's why we have to specify index value to get hold of the particular temp/

#TODO 3: Creating a Dataframe from scratch.

# student_data={
#     'Student_name':['Nisha','Madhuri','Jack','Thomas','Peacemaker'],
#     'Marks':[99,78,87,67,77],
# }

# student_file=pandas.DataFrame(student_data)       #this will convert this data into dataframe structure similar to our spreadsheet.
# student_file.to_csv("student_data.csv")      #this will save the data into csv format into the path you provide , if path doesn't exist it will create a new path.


#TODO 4:Creating a new csv file from squirrel census which will have fur color(from primary fur color) and count.
import pandas
squirrel=pandas.read_csv('004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv') 
fur_color=squirrel['Primary Fur Color']
# print(fur_color.unique())          #checking all the distinctive values present in the list.
gray=fur_color[fur_color=='Gray'].count()          #counting each color count separately using series.count method.
red=fur_color[fur_color=='Cinnamon'].count()
black=fur_color[fur_color=='Black'].count()
squirrel_data={'Fur Color':['gray','red','black'],    #adding the data we fetched into a dictionary in order to later convert it into a csv file
               'Count':[gray,red,black],
}

squirrel_count=pandas.DataFrame(squirrel_data)
squirrel_count.to_csv("squirrel_count.csv")

from tkinter import *
import pandas
#Constants
FONTNAME="SF Mono"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


# def save():
#     web=[entry_website.get()]
#     em=[entry_email.get()]
#     pas=[entry_pass.get()]
    
#     data_dict={
#         "website":[web],
#         "Email":[em],
#         "Password":[pas],
#     }
#     pass_file=pandas.DataFrame(data_dict)
#     try:
#         # Try to read existing file and append
#         existing_data = pandas.read_csv("data.txt", index_col=0)  #index col ignores the index column .
#         updated_data = pandas.concat([existing_data, pass_file], ignore_index=True)   #ignore index helps in dataframe to ignore the index value , and just create another line without creating duplicate indexes.
#         updated_data.to_csv("data.txt")
#     except FileNotFoundError:
#         # File doesn't exist, create new one
#         pass_file.to_csv("data.txt")
    
#     # Clear the entries after saving
#     entry_website.delete(0, END)
#     entry_pass.delete(0, END)

# df1 = pandas.DataFrame({"name": ["Alice"], "age": [25]})  # index: [0]
# df2 = pandas.DataFrame({"name": ["Bob"], "age": [30]})    # index: [0]

# Without ignore_index:
#result = pandas.concat([df1, df2])
# Creates:  name   age
#       0   Alice  25
#       0   Bob    30    <- Duplicate index!

# With ignore_index=True:
#result = pandas.concat([df1, df2], ignore_index=True)
# Creates:  name   age
#       0   Alice  25
#       1   Bob    30    <- Clean sequential index


# # Without index_col:
# df = pandas.read_csv("data.txt")
# # Creates:  Unnamed: 0    website    Email    Password
# #           0             google     john@    pass123
# #           1             facebook   jane@    abc456

# # With index_col=0:
# df = pandas.read_csv("data.txt", index_col=0)  
# # Creates:  website    Email    Password
# #           google     john@    pass123
# #           facebook   jane@    abc456