# Descending order...
dict={"bijender":45,"deepak":60,"param":20,"anjili":30,"roshini":50}
dic=dict.values()
print(dic)
num=[45,60,20,30,50]
i=0
while i<len(num):
    a=i
    j=i+1
    while j<len(num):
        if num[a]<num[j]:
            a=j
        j=j+1
    num[i],num[a]=num[a],num[i]
    i+=1
print(num)
