# -*- coding: utf-8 -*-
"""calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/161Xzx8UX96TufURv__bEAoZe7br8G5O1
"""

def add(a,b) :
  answer = a + b
  print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a,b) : 
  answer = a - b
  print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")
 
def mul(a,b) : 
   answer = a * b
   print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a,b) :
  answer = a / b
  print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")
while True :
  print("A . Addition")
  print("B . Subtraction")
  print("c . multiplication")
  print("D . Division")
  print("E . Exit")


  choise = input("input your choise: ")
  if choise == "a" or choise == "A" :
    print("Addition")
    a = int(input("input first number : "))
    b = int(input("input second number : " ))
    add(a,b)
  elif choise == "b" or choise == "B" :
    print("subtraction")
    a = int(input("input first number : "))
    b = int(input("input second number : " ))
    sub(a,b)
  elif choise == "c" or choise == "C" :
    print("multiplication")
    a = int(input("input first number : "))
    b = int(input("input second number : " ))
    mul(a,b)
  elif choise == "d" or choise == "D" :
    print("division")
    a = int(input("input first number : "))
    b = int(input("input second number : " ))
    div(a,b)
  elif choise == "e" or choise == "E" :
    print("program ended")
    quit()