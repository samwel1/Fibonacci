'''
Fibonacci

The Fibonacci sequence is one of the most famous formulas in mathematics.
Each number in the sequence is the sum of the two numbers that precede it.
For example, here is the Fibonacci sequence for 10 numbers, starting from 0: 0,1,1,2,3,5,8,13,21,34.

The program to takes N (variable num in code) 
positive numbers as input, and recursively calculate and output the first N numbers of the Fibonacci sequence (starting from 0).
'''

num = int(input())

 #Define the recursive function
def fibonacci(n):
    
    #Define the base case n<=1
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


#Iterating over the input
for i in range(num):
    print(fibonacci(i))

fibonacci(num)
