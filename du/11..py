a= int (input('a='))
b= int (input('b='))
c= int (input('c='))


if a>b>c or a>c or a>c>b or b==c and a>b and a>c:
    print ('a je najvacsie')
if b>a>c or b>a>c or b>a or a==c and b>a and b>c:
    print ('b je najvacsie')
if c>a>b or c>b>a or b==a and c>a and c>b:
    print ('c je najvacsie')
if a==b==c:
    print ('su rovnake')