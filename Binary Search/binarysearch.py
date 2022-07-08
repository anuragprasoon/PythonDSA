def binarysearch(list,key):
    l=0
    h=len(list)-1
    while l<=h:
        mid=(l+h)//2
        if key==list[mid]:
            return mid
        elif key< list[mid]:
            h=mid-1
        else:
            l=mid+1

l=[23,1,4,2,4,3]
l.sort()
print(l)
k=int(input("key: "))
s=binarysearch(l,k)
index1=[s,]
i=s-1
while i>=0:
    if l[i]==k:
        index1.append(i)
    else:
        break
    i-=1
i=s+1
while i<len(l):
    if l[i]==k:
        index1.append(i)
    else:
        break
    i+=1
index1.sort()
print(index1)
