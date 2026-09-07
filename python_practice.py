# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 
# %% ###########################################################

#Reilly Hiner (mew2ze)
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
Start
sum = 0                                 #starting value of the fibonacci sequence is 0
first = 0
second = 1

N = input("Enter an integer:")          #this will get the user to enter a number to be used in future code
for i 1 to N
    sum = sum + first                   #adds existing value of sum to first number in sequence
    sum = sum + second
    sum = sum +....
    sum = sum + N                      #continues for N
print(sum)                             #returns value of sum (N sequence in fibonacci)


"""

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6 # the place in the sequence that we want the code to run to

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # runs through numbers 0 to N
total = 0 #sums values over N to return fibonacci sum at N

while count < N: #runs while the value of count is less than N
    total = total + a #adds value of a to existing total

    next_value = a + b #creates new variable which produces the next number in the sequence
    a = b #sets first number to the second number of the previous loop
    b = next_value #sets b to the new value created by adding previous 2 numbers

    count = count + 1 #increases count by 1

print(total) #returns value of fibonacci numbers summed over N

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.
import numpy as np
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
standard_deviation = np.std(fibonacci)
print(standard_deviation)
# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.
N = [5, 10, 15, 20, 25, 30] #numbers to find sums for
Outputs = [] #empty list that will return output


for numbers in N: #iterates over list N
    total = 0 #these values reset each time a new number in the list is used
    count = 0
    a = 0
    b = 1
    while count < numbers: #this section is the same as above with different variable names
        total = total + a 
        new_number = a + b
        a = b
        b = new_number
        count = count + 1
    Outputs+=[total]   #this adds the total for each value to the output list #typeerror, can not add int to list

print(Outputs) #returns output list with all sums




# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = "0"
    b = "1"

    while a <= limit:
        next_value = a + b
        a = b
        b = next_value
        index += 1

    return index


result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_even_fib(limit):
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 == 0:  # This line checks if the Fibonacci number is even
            total = b
        a, b = b, a + b
    return total


# Add your test cases here

# %%
