# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
d = dict()

# enter name and number by separate space
for i in range(0, n):
    name, number = input().split()
    d[name] = number
# print(d)      #print dict, if needed

# enter name in order to get phone number
for i in range(0, n):
    try:
        name = input()
        if name in d:
            print(f"{name}={d[name]}")
        else:
            print("Not found")
    except:
        break
