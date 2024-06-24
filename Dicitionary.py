'''# In Dicitionary it will key '' and Value pair
j={"Muthu":1,"ram":2}
print(type(j))'''

dict={'a':"Muthu",'b':"Using Youtube",'c':1234,'d':12345}
'''print(dict)
print(len(dict))'''

'''#for printing only key data
for i in dict:
    print(i)

    (or)
for i in dict.keys():
    print(i)'''


'''#for printing only values
for i in dict.values():
    print(i)'''

#for changing the valuesin the dictionary
'''print(dict)
dict['a']=1
print(dict)
dict['c']="Changed number"
print(dict)'''
    

#How to add new data in the dicitionary
dict["e"]="Newvalues"
print(dict)

#How to remove the key
dict.pop("a")
print(dict)

#How to clear enterly
dict.clear()
print(dict)
