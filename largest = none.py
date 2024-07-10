largest = None 
smallest = None 
sum = 0 
count = 0 
while True: 
    temp = input('Enter a number') 
    if temp == 'done':
        break
    try: 
        a = int(temp)
    except:
        print ("ban ngu vai lon")
        continue

    if largest is None:
        largest = a
    elif largest < a:
        largest = a 
    if smallest is None: 
        smallest = a 
    elif smallest > a:
        smallest = a
    count = count + 1 
    sum = sum + a 
print ( largest, smallest, sum/count)