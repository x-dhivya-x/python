
def print_message(name):    #define a function 
        print(f"Welcome {name}!")
        print("Ready to learn Python")
print_message("Dhivya")         #calling a function


def add(x,y):  #passing parameter 
        print(x+y)
  
add(20,10)  #passing aguments  #positional arguments


def sub(a,b):
        print(a-b)
sub(a=20,b=4)   #keyword arguments



def square(num):
        return(num*num)         #return the value
print(square(5))