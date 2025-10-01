a= int (input('a='))
b= int (input('b='))
c= int (input('c='))

if a+b>c and a+c>b and b+c>a:
    print ('je to trojuholnik')
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
         print ('je pravouhly')
    elif a==b==c:                       #elif sa vykona iba vtedy ak predchadzajuci if nebol pravdivy
         print ('je rovnostranny')
    if a==b and c!=a or a==c and b!=a or b==c and a!=b: #nedavam elif lebo moze byt trojuholnik pravouhly a zaroven rovnoramenny
          print ('je rovnoramenny')
    #else sa viaze len na posledne if - preto ostatne if dam pod to hlavne if takze else plati na hlavne if (v rovnakej rovine)
else:
    print ('nie je to trojuholnik')