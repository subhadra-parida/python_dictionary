dict1={"name":"Raju","marks":56}
for i in dict1:
    if "name" in dict1:
        print("exists")
    elif "class" in dict1:
        print("not exists")
    else:
        print("nothing")
