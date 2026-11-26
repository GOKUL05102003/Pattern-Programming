n=int(input("enter no. of rows"))
for i in range(n):
    print(" "*i+"*"*(n-i))
'''
n=int(input("Enter no. of Rows: "))
t=0
for i in range(n,0,-1):
    for j in range(t):
        print(" ",end="")
    for k in range(i,0,-1):
        print("*",end="")
    print()
    t+=1
'''
''''
Enter no. of Rows: 5
*****
 ****
  ***
   **
    *
'''