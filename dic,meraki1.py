# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic4={}
# for i in dic1:
#     for i in dic2:
#         dic2[i]=dic2[i]+dic1[i]
#         dic4.update(dic1)
#         dic4.update(dic2)
#         dic4.update(dic3)
#         for i,j in dic1:
            
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}
for i,j in d1.items():
    for k,l in d2.items():
        if i==k:
            d3[i]=(j+l)
            print(d3)
            