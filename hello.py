from datetime import date
print("la fecha de hoy es:" + str (date.today()))

print("Hola mundo")

a = 1
b = 2

print(b+a)

a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")