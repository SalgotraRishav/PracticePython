
"""
Date: June 21st, 2024
Authod: Rishav Salgotra
Language used: Python
Description: This python program checks if the input number is prime or not.
"""
num = int(input("input a number "))

if num <= 1:
    print(str(num), "is not a prime number.")
else:    
    for i in range(2, num):
        if num % i == 0:
            print(str(num),"is not a prime number.")
            break
    else:
        print(str(num), "is a prime number.")