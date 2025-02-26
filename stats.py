def get_num_words(text):

    words_list = text.split()
    words_count = len(words_list)

    return words_count 

def get_num_unique_character(text):

    text = text.lower() # transforms all characters into lowercase
    my_dict = {} # empty dictionnary to count each letter
    
    for character in text:
        if character in my_dict:
            my_dict[character] += 1
        elif character not in my_dict:
            my_dict[character] = 1
        
    return my_dict

def get_alpha_character(my_dict):
    alpha_dict = {}

    for x in my_dict:
        if x.isalpha() == True:
            alpha_dict[x] = my_dict[x] 
        else: 
            continue

    return alpha_dict

def sort_unique_character_count(alpha_dict):    
    tuple_list = list(alpha_dict.items()) #converts dictionnarie into tuple as sort() cant be used on dict. 
    tuple_list.sort(key=lambda x: x[1], reverse=True) # key permet de déterminer le tri sur la valeur du tuple. 

    return tuple_list
