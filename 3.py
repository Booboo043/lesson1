tmpStr = input('please enter string:')
alphaNum=0
numbers=0
spaceNum=0

for i in tmpStr:
    if i.isalpha():
        alphaNum +=1
    elif i.isnumeric():
        numbers +=1
    elif i.isspace():
        spaceNum +=1

print('Letters=%d'%alphaNum)
print('Digits=%d'%numbers)
print('space=%d'%spaceNum)
