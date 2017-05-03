lst = []
c = 0
while True:
    try:
        n = eval(input())
        if n == -1:
            break
        lst.append(n)
        c +=1
        del n      #要把n刪掉，因為如果input輸入n的話，會以為是上一個輸入的數字
    except:
        continue
count = len(lst)
print('%.2f'%sum(lst))
print('%.2f'%(sum(lst)/count))
print(count)
