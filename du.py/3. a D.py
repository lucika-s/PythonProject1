a= int (input('a='))
b= int (input('b='))
c= int (input('c='))

if c>a and c<b or c==a and c==b or c<a and c>b:
        print('c = patri do intervalu')
elif c==a or c==b:
        print('c = patri do intervalu')
else:
    print('c = nepatri do intervalu')