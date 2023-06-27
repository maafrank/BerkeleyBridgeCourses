 


def interleave(A: str=None, B: str=None) -> list:
    power2list = [2**j for j in range(1,8+1)]
    if B == None:
        while len(A) not in power2list:
            A += "."
        B = A[int(len(A)/2):]
        A = A[:int(len(A)/2)]
    print(A, B)
    C = ""
    for a, b in zip(A,B):
        C += a
        C += b
    return C


#A = "abcde"
#B = "12345"
#C = interleave(A=A, B=B)
#print(C)


A = "Hello World!"
C = interleave(A=A)
print(C)
c = interleave(A=C)
