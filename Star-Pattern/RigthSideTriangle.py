n=int(input("enter no. of Rows: "))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
'''
n=int(input("Enter no. of Rows: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()
'''
'''
Enter no. of Rows: 5
    *
   **
  ***
 ****
*****
'''