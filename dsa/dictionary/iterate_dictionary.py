def iterate_dictionary(a) :
    
    """
    discription : Write a Python program to iterate over dictionaries using for loops.
    """
    for key , value in a.items() :
        print(f"key is : {key}, value is : {value}")
    
if __name__ == '__main__' :
    new_dict = {
        "apple" : 4,
        "mango" : 2,
        "kiwi" : 1,
        "orange" : 5,
    }
    
    iterate_dictionary(new_dict)