# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
t=int(input())
def isPrime(data):
    if int(data) < 2:
        return False
    v=int(math.sqrt(data))
    for i in range(2,v+1):
        if data%i==0:
            return False;
    return True;
for i in range(int(input())):
    if isPrime(t):
        print ("Prime")
    else:
        print ("Not prime")
