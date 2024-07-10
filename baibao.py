str1 = open("E:\\text\\chap7'.txt", "r", encoding = "utf-8") 
try: 
    a = str1.read()
    print (a)
finally:
    str1.close()
str2 = open("E:\\text\\chap7''.txt", "r", encoding = "utf-8")
b = str2.read()
print(b)


with open("E:\\text\\chap7'.txt", "r", encoding = "utf-8") as file:
    for line in file: 
        print(line)