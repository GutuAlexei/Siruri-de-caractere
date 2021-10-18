alfabet='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
a1=''
b1=''
c1=''

for q in alfabet:
    x=chr(ord(q)+1)
    a1+=x
    a=a1.replace('!', '')
    b=a.replace('[', 'A')

print('a)', b)

b1=b
for W in alfabet:
    u=b1.replace('Z', 'A')
    h=u.replace('!', '')
    g=h.replace('[', 'A')
print('a)', g)

print(alfabet.replace(' ', '-', len(alfabet)))
