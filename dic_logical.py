dict=["rani","lucky","shalu","swapna","rajshri","rani","rajshree","shalu"]
i=0
s=[]
while i<len(dict):
    j=0
    count=0
    while j<len(dict):
        if dict[i]==dict[j]:
            count=count+1
        j=j+1
    if dict[i] not in s:  
        s.append(dict[i])
        s.append(count)
    i=i+1
print(s)
print(set(s))
