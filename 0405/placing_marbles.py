a = int(input())
length = len(str(a))
counter = 0
for i in range(0,length):
    if int(str(a)[i])%2==1:
        counter+=1
print(counter)