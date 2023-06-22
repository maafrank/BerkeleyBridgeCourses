 
"""
Write a script that prompts the user for their phone number, x. Then carry out the following steps:

 
1. Compute x minus the sum of the digits of x. Call this result y. (hint: to find the sum of the digits of x, check to see what x//10 and x%10 give you)

2. Compute the sum of the digits of y, and store the result back in y.

3. Repeat step 2 until y has just one digit, then display it.
"""

def str2int_sum(num: str) -> None:
    tot = 0
    for n in num:
        tot += int(n)
    return tot

#phone_number = input("Please enter a phone number:")
phone_number = "3104131340"
phone_sum = str2int_sum(phone_number)

y = str(int(phone_number) - phone_sum)

while len(y) > 1:
    phone_sum = str2int_sum(y)
    y = str(int(y) - phone_sum)
print(y)
