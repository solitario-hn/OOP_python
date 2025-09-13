# class User:                      #init functions is an object constructor.
#     def __init__(self):       #here self is the actual object that;s being created or initialized.
#         print("new user is being created...")       #we can now use self=user1 to add attributes to our object recognized here as self.
#         self.id=input("Enter user id: ")
#         self.username=input("Enter the username: ")
#         self.password=input("Enter the user password: ") 

# is_on=True
# while is_on:        
#     user1=User()
#     choice=input("do you wish to add more users 'y' or 'n' ")
#     if choice=='y':
#         pass
#     else:
#         is_on=False
        

# print(user1)            


# question_bank=[]
# for i in range(0,len(question_data)):
#     que=question_data[i]
#     ques=que["text"]
#     ans=que["answer"]
#     new_q=Question(ques,ans)
#     dict={"text":new_q.question,"answer":new_q.answer}    #this individually retrieves the text data from each dictionary 
#                                                                    and puts it into a new dict and then append that dic into our question bank.
#     question_bank.append(dict)
