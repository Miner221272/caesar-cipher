Input = input("what is the message: ")
shift = input("what is the shift space: ")
alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
sting = []
endARR = []
endSTR = ""
for  i in Input:
    strr = str(i)
    sting.append(strr)
print(sting) 
shift = int(shift)
if int(shift) > 26:
    shift = shift - 26
print(shift)
place = 0
for i in sting:
    if i == ' ':
        endARR.append(' ')
    else:
        temp = i
        num = 26 - alphabet.index(str(i)) - shift
        try:
            
            endARR.append(alphabet[alphabet.index(str(i)) + shift])
        except IndexError:
            endARR.append(alphabet[alphabet.index('a') + num])
            print(alphabet[alphabet.index('a') + num])
for i in endARR:
    endSTR = endSTR + i
print(endSTR)