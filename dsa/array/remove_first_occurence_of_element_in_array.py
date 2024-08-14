def remove_first_occur(arr, ele) :
    
    """
    description : Write a Python program to remove the first occurrence of a specified element from an
    array.
    """
    
    new_array = arr
    for i in range(len(arr)) :
        if new_array[i] == ele:
            new_array.remove(new_array[i])
            return new_array
    
if __name__ == '__main__' :
    arr = [2, 4, 2, 3, 4]
    ele = 4
    new_array = remove_first_occur(arr, ele)
    print(f"new output" ,new_array)