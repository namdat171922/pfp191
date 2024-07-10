def letter_frequency(text): 
    frequency_dict = {} 
    for char in text: 
        if char.isalpha(): 
            char =  char.lower() 
            if char in  frequency_dict: 
                frequency_dict[char] = frequency_dict[char] + 1 
            else: 
                frequency_dict[char] = 1
    return frequency_dict 
text = ' banana ' 
print(letter_frequency(text))