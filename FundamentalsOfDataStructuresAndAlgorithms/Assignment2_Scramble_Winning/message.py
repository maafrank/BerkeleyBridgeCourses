 


#def interleave(A: str=None, B: str=None) -> list:
#    power2list = [2**j for j in range(1,8+1)]
#    if B == None:
#        while len(A) not in power2list:
#            A += "."
#        B = A[int(len(A)/2):]
#        A = A[:int(len(A)/2)]
#    print(A, B)
#    C = ""
#    for a, b in zip(A,B):
#        C += a
#        C += b
#    return C

#A = "abcde"
#B = "12345"
#C = interleave(A=A, B=B)
#print(C)

def interleave(A: str=None, B: str=None, Done=False) -> list:

    # pad with '.'
    # break down single statment into 2
    power2list = [2**j for j in range(1,8+1)]

    if B == None:
        while len(A) not in power2list:
            A += "."
        B = A[int(len(A)/2):]
        A = A[:int(len(A)/2)]
        
    # recursively break down until sets of 2
    if not Done:
        if len(A) == 4: Done = True
        else: Done = False
        b = A[int(len(A)/2):]
        a = A[:int(len(A)/2)]
        A, Done = interleave(a, b, Done=Done)

        if len(B) == 4: Done = True
        else: Done=False
        b = B[int(len(B)/2):]
        a = B[:int(len(B)/2)]
        B, Done = interleave(a, b, Done=Done)
        
        C, Done = interleave(A, B, Done=Done)
        if Done: return C, Done
    else:
        C = ""
        for a, b in zip(A, B):
            C += a
            C += b
        return C, Done


##########
## MAIN ##
##########
# read input file
f = open("input.txt", "r")
my_outputs = []
for x in f:
    C, _ = interleave(A=x.strip())
    my_outputs.append(C)

# read output file
f = open("output.txt", "r")
outputs = []
for x in f:
    outputs.append(x.strip())

for x, y in zip(my_outputs, outputs):
    print(f"{x} == {y} {x==y}")
