#Samantha Patin and Mandy Guo

#Finding and replacing a substring within a string

def replace_substring(main, remove, replace):
    output=[]
    index=0
    while index<len(main):
        if main [index: index+len(remove)]==remove:
            index += len(remove)
            output.append(replace)
        else:
            output.append(main[index])
            index+=1
    print("".join(output))

main="Cats are amazing creatures. Cats are cool."
remove="Cats"
replace="Dogs"


replace_substring(main, remove, replace)
