# Take input of name and marks of 10 students and store to a dictionary.
dic={'sonu':85,'Kartik':90,'Deepak':96,'Aman':76,'Somesh':60,'Umesh':85,'Amarpal':70,'Roshan':57,'Riyaz':98,'Shabid':56}
dict1={}
i=1
while i<=10:
    a=input("enter your keys=")
    b=int(input("enter your values="))
    dict1[a]=b
    i=i+1
print(dict1)
