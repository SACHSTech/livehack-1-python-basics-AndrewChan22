'''
-------------------------------------------------------------------------
Name:		problem2.py

Purpose: User inputs number of students and number of available pieces of Popeyes chicken. The program then calculates how many pieces of student will receive, while Mr. Fabroa receives the remaining pieces of chicken

Author:	Chan. A

Created:	date in 12/07/2020
-------------------------------------------------------------------------
'''
# intro
print("Mr. Fabroa's class won a contest!")

# user inputs number of student
students = int(input("Enter the number of students in class: "))

# user inputs number of available pieces of chicken
chicken_pieces = int(input("Enter how many pieces of Popeyes chicken are available?: "))

# how many pieces each student will receive
print("Each student will get " + str(chicken_pieces//students) + " pieces of Popeyes chicken.")

# how many pieces of chicken Mr. Fabroa will receive
print("Mr. Fabroa will get " + str(chicken_pieces%students) + " piece(s) of the remaining Popeyes chicken.")