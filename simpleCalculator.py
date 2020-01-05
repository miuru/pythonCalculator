#my Calculator

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

def main():
    print(" Welcome to my simple calculator ")
    print ("")
    operation = input("What do you want me to do ? ( + , - , * , / )");
    #invalid Operation
    if(operation != "+" and operation != "-" and operation != "*" and operation != "/"):
        print("Invlid Operation , I can only do + ,-,*,/ , Please select one of these ");
        main()

    else:
        var1 = int(input("Enter Number 1 : "))
        var2 = int(input("Enter Number 2 : "))

        if(operation == "+"):
            print("Your Answer is  : ")
            print(add(var1,var2))
            print("")     
            main()
        elif(operation == "-"):
            print("Your Answer is  : ")
            print(sub(var1,var2))
            main()
        elif(operation == "*"):
            print("Your Answer is  : ")
            print(mul(var1,var2))
            main()
        elif(operation == "/"):
            print("Your Answer is  : ")
            print(div(var1,var2))
            main()

main()

    
