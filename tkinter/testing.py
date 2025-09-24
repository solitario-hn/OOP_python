#UNDERSTANDING * ARGS  multiple arguments.
def add(*args):
    print(type(args))              #args is saved in a tuple (9,8,,7,6...) <class 'tuple'>
    sum=0
    for n in args[1:]:  #now it will start from 1 
        sum+=n
    return sum

print(add(9,8,7,6,5,0,9,8,7,43,65,98,70))

#UNDERSTADING **KWARGS multiple keyword arguemnts.
def calculate(n,**kwargs):      #this will allow us to call the func as pass one mandatory argument (n) and other optional multiple keyword args.
    
    print(type(kwargs))   #kwargs is saved in the form of a dict <class 'dict'> where {"add":5 , "subtract":0} keyword arg keyword=dict key , and its value =dict key value correspondent to it.
#     n-=kwargs['subtract']
#     n*=kwargs['multiply']
    n=kwargs.get('addition')   #this will allow to go into dict i.e. kwargs and tap into the key addition's value
    print(n)
    
calculate(5,subtract=0,multiply=5) #right now if i miss one of they kwargs and call it inside the function it will give me an key error , as it would not be able to find tht key inside the dict.
#we can solve this by using kwargs.get("add") get method will return none if it doesn't find the value but in tht case none is not a integer , so it will not be able to use '+' mathematical operrtaions.
class Calculate:
    def __init__(self,**kwargs):
        # self.add=kwargs["add"] will give out error if it doesn't find add in kwargs dict i.e. we don't pass add as a keyword arg.
        self.add=kwargs.get("addition")
        self.subtraction=kwargs.get("subtraction")
        self.method='TO CALCULATE'
        
calc=Calculate(addition=90)
print(calc.add)                    #90 as we passed 90 in addition keyword arg    , PRINTS '90'
print(calc.subtraction)            #as we didn't passed any subtrcation argument .get will return None here . print's 'None'
print(calc.method)                 #prints 'TO CALCULATE' the default value we set.

