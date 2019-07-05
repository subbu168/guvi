wo= int(input())
c=[]
for i in range(0,wo):
 inpu=input()
 c.append(inpu)
li=[]
for i in zip(*c):
 if(i.count(i[0])==len(i)):
  li.append(i[0])
 
 else:
  break
print(''.join(li))
