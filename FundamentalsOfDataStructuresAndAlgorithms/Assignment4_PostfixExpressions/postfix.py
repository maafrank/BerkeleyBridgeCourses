

def postfix(expression: str) -> int:

    expression = expression.replace(" ", "")
    num_stack = []

    for char in expression:
        print(num_stack, char)
        if char in ["+", "-", "*", "/"]:
            B = num_stack.pop()
            A = num_stack.pop()
            if char == "+":
                num_stack.append(A+B)
            elif char == "-":
                num_stack.append(B-A)
            elif char == "*":
                num_stack.append(A*B)
            elif char == "/":
                num_stack.append(A/B)
        else:
            num_stack.append(int(char))
    return num_stack[0]


input = "2 2 8 4 5 / 6 * * 3 4 / 5 * + + 5 - 2 * 10 + +"
z = postfix(input)
answer = "90.3"
print(z, answer)


## read input file
#f = open("input.txt", "r")
#my_outputs = []
#for x in f:
#    C= postfix(x.strip())
#    my_outputs.append(C)
#
## read output file
#f = open("output.txt", "r")
#outputs = []
#for x in f:
#    outputs.append(float(x.strip()))
#
#for x, y in zip(my_outputs, outputs):
#    print(f"{x} == {y} {x==y}")
