#1.   Student Result System Input marks of 5 subjects.If any subject < 40 → Fail Else calculate percentage and grade.

marks =tuple(map(int,input("enter the marks").split()))
totalmarks=500
failed= False
for sub in marks  :
    if sub<40:
        failed=True
        break
    
if failed:
    print("failed") 
else:
        percentage=(sum(marks)/totalmarks)*100
        print(percentage)
        if percentage>90:
            print("a")
        elif percentage>80:
            print("B")
        elif percentage>70:
            print("c")
        elif percentage>60:
            print("d")
        else:
            print("no grade")




#------------------------------------------------------------------------------------------


# # 5. Number Comparison
# # Input three numbers and print:
# # Largest
# # Smallest
# # Whether all are equal

a,b,c=map(int,input("enter three number ").split())

if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is grater")
elif c>a and c>b:
    print("c is greater")
elif a==b==c:
    print("all are equal")
else:
    print("invalid input")




#--------------------------------------------------------------------------------------------


# # 6. Character Identifier
# # Input a character and identify whether it is:
# # Uppercase letter
# # Lowercase letter
# # Digit
# # Special character

char=input("enter a character")

if char.islower():
    print("lower")
elif char.isupper():
    print("uppercase")
elif char.isdigit():
    print("digit")
elif char in ["!@$%^& *()#"]:
    print("special char")
else:
    print("unknown")


#----------------------------------------------------------------------------------------------------

# 2.  Leap Year with Century Rule Check whether a given year is a leap year considering century year

year=int(input("enter your year"))

if year%400==0 or(year%4==0 and year%100!=0):
    print("leap year")
else:
    print("not a yeap year ")

#---------------------------------------------------------------------------------------------------

# #8.  Bus Fare System Fare based on distance:
# # ≤10 km → ₹10
# # 11–30 km → ₹20
# # 30 km → ₹30
# # Senior citizens get 20% discount.


dist=int(input("enter the distance"))
dist10=10 #under 10kms 
dist20=20# under 30 kms
dist30=30 # 30kms and more 
charges=0
if dist<=10:
    print("charges ordinary== ₹",10 )
    print("Senior citizens",dist10-dist10*0.20)
elif dist>=11 and dist<=30:
    print("charges ==  ₹",20)
    print("Senior citizens",dist20-dist20*0.20)
elif dist>30:
    print("charges== ₹",30)
    print("Senior citizens",dist30-dist30*0.20)
else:
    print("unknowm input")
    




#----------------------------------------------------------------------------------
# #14.  Traffic Signal System
# # Input signal color and print action:
# # Red → Stop
# # Yellow → Ready
# # Green → Go


color=input("enter the color  ")

if color.lower()=="red":
    print("stop")
elif color.lower()=="yellow":
    print("Ready")
elif color.lower()=="green":
    print("GO")
else:
    print("unknown color")



#----------------------------------------------------------------------------------------------




#15.  Time-Based Greeting
# Input time (0–23):
# Morning
# Afternoon
# Evening
# Night


time=int(input("enter time from 0 to 24 hrs format "))

if time>=0 and time<=12:
    print("morning")
elif time>12 and time<16:
    print("afternoon")
elif time>=16 and time<=19:
    print("evening")
elif time>19 and time<=24:
    print("night")
else:
    print("unknown time")


#------------------------------------------------------------------------------------------


# 17. Mobile Recharge Plan
# Recharge amount:
# ₹199 → 1.5GB/day
# ₹299 → 2GB/day
# ₹499 → Unlimited

amount=int(input("enter amount"))

if amount==199:
    print("1.5GB/day +unlimited calls")
elif amount==299:
    print(" 2GB/day + unlimited calls")
elif amount==499:
    print("unlimited" )
else:
    print("invalid amount")



#--------------------------------------------------------------------------------------



# 12. Weather Advisory System
# Input temperature:
# <10 → Very Cold
# 10–20 → Cold
# 21–30 → Warm
# 30 → Hot



# temp=int(input("enter temperature"))

if temp<=10:
    print("very cold")
elif temp>10 and temp<=20:
    print("cold")
elif temp>20 and temp<=30:
    print("warm")
elif temp>30:
    print("hot")
else:
    print("enter valid input")

#---------------------------------------------------------------------------------------------



























































# # 7. Password Strength Checker
# # Input password and check:
# # Minimum 8 characters
# # Contains digit and special character



# password=input("enter a password 8 char")

if len(password)>=8:
    if password in ["1234567890"]:#--------------------------------------------error
        if password in ["!@#$%^&*()"]:
            print(password)
        else:
            print("must have special character")
    else:
        print("must have one numberr")
else:
    print("length should be more than 8")


