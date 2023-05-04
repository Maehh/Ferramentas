
def dictgen(*args) :
    simpledict = {}
    cont = 1            # Each value gets it's own key 
    Add = 'Key '

    for i in args :          
        simpledict.setdefault(Add + str(cont), i)
        cont += 1
    return simpledict

# Use example
mydict = dictgen('Abc', 12, ['Abcde', 0], 'Mark')
print(mydict)