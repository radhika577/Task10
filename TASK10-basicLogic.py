# Finding the profit percentage using sp and cp

# sp=int(input("Enter Selling Price :"))
# cp=int(input("Enter Cost Price :"))
# profit=sp-cp
# print("profit =",profit)
# profit_percentage=(profit/cp)*100
# print(profit_percentage,"%")

# Finding missing angle in triangle by using two given angles

# a1=int(input("Enter angle 1 :"))
# a2=int(input("Enter angle 2 :"))
# sum=a1+a2
# a3=180-sum
# print("The Missing Angle of Triangle",a3)


#find last digit of given number

# n=int(input("Enter the number :"))
# last_digit=n%10
# print("The Last digit of given number is :",last_digit)


# Remove Last digit from given number

# n=int(input("Enter the Number :"))
# remove_last_digit=n//10
# print("After removing last digit of given number :",remove_last_digit)


# Find the first digit of 4-digit number

# n=int(input("Enter the 4-digit Number :"))
# first_digit=n//1000
# print("First digit of 4-digit number is :",first_digit)


# Find sum of first n natural numbers vthout loop

# n=int(input("Enter the first n Natural Numbers :"))
# sum_of_first_natural_numbers=n*(n+1)//2
# print("Sum of First n Natural Numbers is :",sum_of_first_natural_numbers)


# Find the avg of first n Natural Numbers

# n=int(input("Enter the first n natural numbers :"))
# avg_of_first_natural_numbers=(n+1)/2
# print("Average of First n Natural Numbers is :",avg_of_first_natural_numbers)


# Find gross salary using basic salary, bonus , incentive

# salary=20000
# bonus_per=20
# incen_per=5
# bonus=bonus_per/100*salary
# incentive=incen_per/100*salary
# print("bonus =",bonus)
# print("incentive =",incentive)
# gross_salary=salary+bonus+incentive
# print("Gross Salary =",gross_salary)


#find in_hand salary using salary,bonus,incentive,pf,health_insurance

# salary=20000
# bonus_per=20
# incen_per=5
# pf_per=2
# health_insu_per=1
# bonus=bonus_per/100*salary
# incentive=incen_per/100*salary
# print("Bonus =",bonus)
# print("Incentive =",incentive)
# gross_salary=salary+bonus+incentive
# print("Gross Salary =",gross_salary)
# pf=pf_per/100*salary
# health_ins=health_insu_per/100*salary
# in_hand_salary=gross_salary-pf-health_ins
# print("In Hand Salary =",in_hand_salary)


#swap numbers with 3-variables

# a=10
# b=20
# print("Before Swapping")
# print("a =",a)
# print("b =",b)
# c=a
# a=b
# b=c
# print("After Swapping")
# print("a =",a)
# print("b =",b)


#swap with 2-variables
# a=10
# b=20
# print("Before Swapping")
# print("a =",a)
# print("b =",b)
# a=a+b
# b=a-b
# a=a-b
# print("After Swapping")
# print("a =",a)
# print("b =",b)


a=10
b=20
print("Before Swapping")
print("a =",a)
print("b =",b)
a=a*b
b=a//b
a=a//b
print("After Swapping")
print("a =",a)
print("b =",b)

