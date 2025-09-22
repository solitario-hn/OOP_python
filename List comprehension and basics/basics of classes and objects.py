# from turtle import Turtle ,Screen  #importing Turtle(pascal case) class from turtle module
# timmy=Turtle()
# print(timmy)  #will return output of shwoing object turtle 

# my_screen=Screen()    -using the screen class present in turtle module , to create a new project my_screen
# print(my_screen.canvheight)    -this will use canvheight attribute present in screen class =stored in myscreen object
#                                -prints screen height 300
                                                           
# timmy.shape("turtle")
# timmy.color("DeepPink2")
# timmy.forward(100)
# timmy.left(60)
# timmy.back(10)
# my_screen.exitonclick()           -shows you the screen of canva and code doesn't stop running until you click on screenn (we use exitonclick [method/function]present inside object myscreen created from class Screen)


# from prettytable import PrettyTable
# table=PrettyTable()
# table.add_column("Pokemon",["Pikachu","Squirtle","Charmander","Bulbasaur","Meow-meow","Jigglypuff"])
# table.add_column("Type",["Electric","Water","Fire","Earth","Magic","Love"])
# table.align='l'                      #accesing a function(attributes) instead of a modifier inside the pretty table.
# print(table) 

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



class User:                      #init functions is an object constructor.
    def __init__(self,id,username,password):       #you can also add more parameters after self to add attributes to your object.
        print("new user is being created...")      
        self.username=username                        #using self=object to add attributes wrt to the paramters passed.
        self.password=password
        self.id=id
        self.followers=0 #this will set the gender as not prefer to say as a default value.
        self.following=0
    
    def follow(self,user):       #in classes methods(functions) always take self(the one calling the method/func) as the first parameter.
        user1.followers+=1       #will change user1
        self.following+=1                #will change the self(object which will call the funct method.)


is_on=True
while is_on:        
    id1=input("Enter user id: ")
    username1=input("Enter the username: ")
    password1=input("Enter the user password: ") 
    user1=User(id1,username1,password1) #ignoring self since self is user1 object initialized itself and passing rest of the paramters.                   
    user2=User(id1,username1,password1)
    choice=input("do you wish to add more users 'y' or 'n' ")
    if choice=='y':
        pass
    else:
        user1.follow(user2)
        is_on=False
       

    print(user1.id)      

#import turtle as t    we can now use 't' instead turtle , e.g. t.Turtle() to create an object
# from turtle import * #imports everything from the module using * it's
# great but gets very confusing sometimes due to mix of diff func present in module and we become unable to know it's orgin and doing