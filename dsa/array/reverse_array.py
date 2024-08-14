def reverse_array(arr) :
    """
    description : Write a Python program to reverse the order of the items in the array.
    """
    reverse_array = []
    for i in range (len(arr)-1, -1, -1) :
        reverse_array.append(arr[i])
    return reverse_array
  
    
if __name__  == '__main__' :
    arr = [1,2,3,4,5]
    print(reverse_array(arr))