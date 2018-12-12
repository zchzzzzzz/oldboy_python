user_list=[
    {"username":"a","login":True,"passwd":"111"},
    {"username":"b","login":False,"passwd":"222"},
    {"username": "zzz", "login": False,"passwd":"123"}
]
for i in range(user_list.__len__()):
    a = user_list[i]["username"]
    b = user_list[i]["login"]
    c= user_list[i]["passwd"]
    if user_list[i]["username"] and user_list[i]["login"]:
        print(a)
    else:
        if (a=="zzz") & (c== "123"):
            user_list[i]["login"] = True
            print("-----")
            print(a)