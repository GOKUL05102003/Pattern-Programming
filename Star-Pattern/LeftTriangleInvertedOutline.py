n=int(input("Enter the no. of Rows: "))
for i in range(n,0,-1):
    print((("*"*n) if(i==n)else "*"+" "*(i-2)+"*" if(i!=1)else "*"))
'''
n=int(input("Enter the no. of Rows: "))
for i  in range(n,0,-1):
    for j in range(i,0,-1):
        if i==n or i==j or j==1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
'''
Enter the no. of Rows: 5
*****
*  *
* *
**
*
'''