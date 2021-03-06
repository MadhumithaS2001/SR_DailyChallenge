'''
String Matrix & Character Matrix 

The program must accept a matrix of size R*C and the position of a cell (X, Y) in the matrix as the input.
The matrix contains string values where the length of each string is always a perfect square.
The program must print the characters of the string value that occurs in the position (X, Y) as a square matrix. 
Boundary Condition(s): 
2 <= R,C <= 50
1 <= Length of each string <= 100 
1 <= X <= R 
1 <= Y <= C 

Input Format:

The first line contains R and C separated by a space. 
The next R lines, each contains C string values separated by a space.
The (R+2)th line contains X and Y separated by a space. 

Output Format:

The lines containing the characters of the string value that occurs in the position (X, Y) as a square matrix.

Example 
Input/Output 1:

Input: 
3 3 
four char skillrack
days education well 
nutrition moon ELECTROGALVANIZE 
2 2 

Output: 
e d u 
c a t 
i o n 

Explanation: 
Here X=2 and Y=2, the string value that occurs in the position (2, 2) in the given matrix is education.
The length of the string education is 9.
So the characters in the string are printed as a square matrix of size 3*3.
e d u 
c a t 
i o n 

Example 
Input/Output 2:

Input:
3 3 
four char skillrack
days education well
nutrition moon ELECTROGALVANIZE
3 3 

Output:

E L E C T
R O G A L
V A N I Z E

'''

import math
n,m=map(int,input().split())
lis=[]
for i in range(n):
    lis.append(list(map(str,input().split())))
x,y=map(int,input().split())
sq=lis[x-1][y-1]
s=len(sq)
ms=int(math.sqrt(s))
for i in range(ms):
    print(*(list(sq[:ms])))
    sq=sq[ms:]


