f1 = open('C:\\Users\\CCKing\\Downloads\\score.txt','r')
data = f1.readlines()
f1.close()
MathEngPass=[]
Fail = []

for i in range(len(data)):
    data[i]= data[i].strip()
    data[i]=data[i].split(',')
for i in range(1,len(data)):
    if int(data[i][1])>= 60 and int(data[i][2])>= 60:
        MathEngPass.append(data[i][0])
    if int(data[i][1])+int(data[i][2]) <120:
        Fail.append(data[i][0])

Total = len(data)-1

MathEngPass.sort()
Fail.sort()

print(MathEngPass)
print(Fail)
print(Total)
