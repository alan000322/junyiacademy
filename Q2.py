#### Param & Var
num = int(input("Input: "))
result = ""
count = 0

#### Main
for n in range(1, num+1):
    if  (n%3 == 0 or n%5 == 0) and n%15 != 0 : continue
    result += str(n)
    count += 1
    result += ", "
result = result.rstrip(", ")
print(str(num) + '以內，非3、非5的倍數，但為15的倍數的有：\n' + result + '\n')
print('總數:\t' + str(count))