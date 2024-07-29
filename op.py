def sum(x,y):
    return x+y

def sub(x,y):
    return x-y

def multi(x,y):
    return x*y

def divide(x,y):
    return x/y

a = float(input("Enter the number:"))
b = float(input("Enter the number:"))
z = input("Enter the operaters:")

if(z == '+'):
    print("Sum =",add(a,b))

elif(z == '-'):
    print("Subraction =",sub(a,b))

elif(z == '*'):
    print("Multiplication =",multi(a,b))

elif(z == '/'):
    print("Division =",divide(a,b))

else:
    print("Please enter the valid operators!!")
    
