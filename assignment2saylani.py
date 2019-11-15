"""1. Write a program which takes 5 inputs from user for different subject’s
marks, total it and generate mark sheet using grades ? """

urdu = input("Urdu subject marks: ") 
english = input("English subject marks: ")
math = input("Math subject marks: ")
ai = input("AI subject marks: ")
pythonz  = input("Python subject marks: ")
total = 500
sums = int(urdu) + int(english) + int(math) +  int(ai) + int(pythonz)
per = (sums*100) / total;
print("Percentage: ", per)

if(per >= 90) :
    grade = "Grade A+"
elif(per >= 79 and per <= 89):
    grade = "Grade A"
elif(per >= 70 and per <= 78):
    grade = "Grade B+"
elif(per >= 60 and per <= 69):
    grade = "Grade B"
elif(per >= 50 and per <= 59):
    grade = "Grade C"
else : 
    grade = "Fail"
print("""\t*********************************************
      \tUrdu subject marks: {} 
      \n\tEnglish subject marks: {} 
      \n\tMath subject marks: {}
      \n\tAI subject marks: {}
      \n\tPython subject marks: {}
      \n\tTotal Marks: {}  OutOf 500 
      \n\t{}
        *********************************************"""
      .format(urdu, english, math, ai, pythonz, str(sums), grade ))

"""2. Write a program which take input from user and identify that the given
number is even or odd?"""
num = input("Enter Number i'll tell You it's Even Or Odd: ")
if int(num) % 2 == 0:
    print("Given Number is Even: ", num)
else:
    print("Given Number is Odd: ", num)    

"""3. Write a program which print the length of the list?"""
aList = ['sd',2,'ds','43',53,'fd']
print("Lenght of list Using Length Function: ",len(aList))
count = 0
for _ in aList:
    count +=1
print("Lenght of list : ", str(count))     

"""4. Write a Python program to sum all the numeric items in a list?"""
snList = ['sd','2','ds','43',53,'fd',10]
summ = 0
for i in snList:
    try:
        numb = float(i)
        summ += int(numb)  
    except:
        pass
print("sum of list integer number is : ", summ)

"""5. Write a Python program to get the largest number from a numeric list."""
lNlist = [34,65,67,899,86,45,6778,5,34,5465,678,9]
nmax = 0
for i in lNlist:
    if i > nmax:
        nmax = i 
print("Largest Number from Numeric List: ", nmax)
print("Using Max Function: ",max(lNlist))    

"""6. Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are
less than 5."""

exList = [2,4,5,6,7,92,44,6,34,2,1,3,3,4,5,6,73,3,1]
less5List = []
for i in exList:
    if i < 5:
        less5List.append(i)
print("List Of Less than 5: ",less5List)
            