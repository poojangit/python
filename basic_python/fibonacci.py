def fibanacci_number(num):
    if num <=1:
        return num
    else:
        return (fibanacci_number(num-1) + fibanacci_number(num-2))
 
if __name__ == "__main__":   
    number = int((input('Enter the number: ')))
    if number<=0:
        print("please Enter the positive number")
    else:
        for i in range(number):
            print(fibanacci_number(i))