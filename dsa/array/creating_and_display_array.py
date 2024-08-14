def display_array(arr) : 
    
    """
    description : 1. Write a Python program to create an array of 5 integers and display the array items.
    Access individual element through indexes.
    """
    
    for i in range(len(arr)) :
        print(arr[i], end = ' ')
    
if __name__ == '__main__':
    arr = [1,2,3,4,5]
    display_array(arr)