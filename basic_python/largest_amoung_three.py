def largest_num(a,b,c) :
    """
    description : finds the largest amoung three numbers
    input : pass any three numbers
    result: largest number
    """
    
    if b < a > c :
        return f" {a} is the largest"
    elif a < b > c :
        return f" {b} is the largest"
    else :
        return f" {c} is the largest"
    
if __name__ == '__main__' :
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    num3 = int(input("Enter third number"))
    
    print(largest_num(num1,num2,num3))