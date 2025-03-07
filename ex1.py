
#1.Write two methods with the same name but different number of parameters of same type an call the methods
a = [3, 23, 3]
try:
    print ("Second element = ",a[1])
 
#if there is an fourth then print this element value
    print ("Fourth element = ",a[3])
    
except:
    print ("An error occurred")

print()
#2. Write two methods with the same name but different number of parameters of different data type and call the methods
bb = [3,2,1]
try:
    a == bb
except:
    print("They are not equal")
else:
    print("Both Equal") 

print()
#3. Write two methods with the same name and same number of parameters of same type
try:
    k = 3/0
    print(k)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print('This is always executed')
