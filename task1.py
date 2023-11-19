def fab():
    a,b=0, 1
    while True:
        yield a
        a,b= b, a+b

#use with an example
z= fab()
y=int(input("Enter the number you want to calculate fabnic series"))
for i in range(y):
    print(next(z))