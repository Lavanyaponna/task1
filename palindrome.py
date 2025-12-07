import time 
str1=input("Enter the string_object:")
if(str1==str1[::-1]):
    print(str1," ",str1[::-1],": Palindrom_Object")
else:
    print(str1," ",str1[::-1],":Not a Palindrom_object")
print()
time.sleep(2)
print("End of an application")