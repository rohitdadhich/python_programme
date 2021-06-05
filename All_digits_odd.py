#all the numbers betweeen 1000 and 3000 where all the digits are odd

for num in range(1000,3000):
    num=str(num)
    count=0
    length=len(num)
    for digit in range (0,length):
        if (int(num[digit])%2!=0):
            count+=1
    if (count==4):
        print(num)
