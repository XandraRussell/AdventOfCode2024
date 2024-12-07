LeftList=[3,4,2,1,3,3]
RightList=[4,3,5,3,9,3]

#order the lists
LeftList.sort()
RightList.sort()

#find difference between lists
ListDif=0
i=0
while i<len(LeftList):
    ListDif=ListDif+abs(LeftList[i]-RightList[i])
    i=i+1

print(ListDif)