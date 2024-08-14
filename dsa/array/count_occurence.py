def count_occurence(array, ele) :
    
    """
    description : Write a Python program to get the number of occurrences of a specified element in an
    array.
    """
    count = 0
    for i in range (len(array)-1, -1, -1) :
        if array[i] == ele:
            count += 1
    return count
    
    
if __name__ == '__main__' :
    array = [1,1,2,3,4,4]
    ele = 4
    print(count_occurence(array, ele))