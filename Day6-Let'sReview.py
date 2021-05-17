# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input().strip())
len_S=[]
for i in range(T):
    S=input().strip()
    len_S.append(S)

for i in len_S:
        str1=[]
        str2=[]
        str =list(i)
        for j in range(len(str)):
            if j % 2 == 0 :
                str1.append(str[j])
            else:
                str2.append(str[j])
        print(''.join(str1),  ''.join(str2))
