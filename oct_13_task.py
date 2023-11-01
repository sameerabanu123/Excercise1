# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
#
# input- score - 89
#
# output- B
#
# A: 90-100
#
# B: 80-89
#
# C: 70-79
#
# D: 60-69
#
# F: 0-59
#
# If, elif, else

score =int(input("Please Enter your Score : "))
if score >= 90 and score <=100:
    print("Grade-A")
elif score <= 89 and score >= 80:
    print("Grade-B")
elif score >= 70 and score <= 79:
    print("Grade-C" )
elif score >= 60 and score<=69:
    print("Grade-D")
else :
    print("Grade-F")

# Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.

#Input = 2024
#Output = Leap year

year=int(input("enter the year:"))
leap_year=["leapyear" if year%4==0 or year%100!=0 and year%400==0 else "not a leap year"]
print(leap_year)

---------------or----------------------------------------

leap_year= int(input("Please enter year: "))
if leap_year%4==0 or leap_year%100!=0 and leap_year%400==0 :
    print (f'{leap_year} is a Leap Year')

else:
    print("Not a Leap year ")

# Write a program that classifies a triangle based on its side lengths.
#
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side 3
s1=int(input("enter the side1:"))
s2=int(input("enter the side2:"))
s3=int(input("enter the side3:"))
if s1==s2==s3:
    print("This is a equilateral triangle")
elif s1==s2 or s2==s3 or s3==s1:
    print("This is a Isosceles triangle")
else:
    print("This is a Scalene triangle")
