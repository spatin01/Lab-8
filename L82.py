#Samantha Patin and Mandy Guo

#Putting each character within a sting into an individual character list:
string="Hello world"
output=[]
index=0
while index<len(string):
    output.append(string[index])
    index+=1

print(output)


#Example SPECIFIC code for find and remove
string="SPAM!HelloSPAM! worldSPAM!"
output=[]
index=0
while index<len(string):
    if string[index:index+5]=="SPAM!":
        index+=5
    else:
        output.append(string[index])
        index+=1

print("".join(output))

#Generic find and remove function

def remove_substring(main, remove):
    output=[]
    index=0
    while index<len(main):
        if main [index: index+len(remove)]==remove:
            index += len(remove)
        else:
            output.append(main[index])
            index+=1
    print("".join(output))

main="CatsDogs are Catscool!Cats!"
remove="Cats"

remove_substring(main, remove)


    
