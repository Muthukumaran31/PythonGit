#create a function name def
'''def paint():
    print("hello")
paint()'''


'''def paint():
    return "I am Muthu"
v=paint()
print(v)'''

Username="muthu"
Password=123
usern=str(input("Enter username:"))
passw=int(input("Enter password:"))

def checking():
    if(Username==usern and Password==passw):
        return True
    else:
        return False
m=checking()
print(m)


