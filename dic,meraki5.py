# Create a dictionary from 2 lists, where the elements of 1st list are the keys
#  and the elements of the 2nd list are the corresponding values.

list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
i=0
a={}
while i<len(list1):
    b=list1[i]
    c=list2[i]
    a[b]=c
    i=i+1
print(a)