
# Take a list having dictionary elements as shown below (Sample Data) and then store all the 
# unique values into a list and print.

dic1=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},
{"six":"9"},{"seven":"7"}]
a=[]
for i in dic1:
    for value in dic1.values():
        if value in a:
            pass
        else:
            a.append(value)
print(a)

