def slice_list(input_list):
    if len(input_list) > 3:
        return input_list[2:]
mylist = [1,2,3,4,5,6,7]
print (slice_list(mylist))