string="ThiS is String with Upper and lower case Letters"
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def count(string,find_letter):
    count=0
    for letter in string:
        if letter.lower()==find_letter.lower():
            count+=1
    return count

for letter in alphabet:
    n=count(string,letter)
    if n>0:
        print("{0} {1}".format(letter,n))

        

# Bonus them cho a cach cach ba dao nay nua :v

##myString = ("ThiS is String with Upper and lower case Letters").lower().replace(" ","")
##print("a",myString.count('a'))
##print("c",myString.count('c'))
##print("d",myString.count('d'))
##print("e",myString.count('e'))
##print("g",myString.count('g'))
##print("h",myString.count('h'))
##print("i",myString.count('i'))
##print("l",myString.count('l'))
##print("n",myString.count('n'))
##print("o",myString.count('o'))
##print("p",myString.count('p'))
##print("r",myString.count('r'))
##print("s",myString.count('s'))
##print("t",myString.count('t'))
##print("u",myString.count('u'))
##print("w",myString.count('w'))
