'''

Diagonal Grids Pattern 

The program must accept an integer N as the input. 
The program must print the N grids of asterisks based on the following conditions. 
	- The program must print an asterisk in the first line. 
	- Then the program must print a grid of asterisks of size 2*2 in the next 2 lines diagonally. 
	- Then the program must print a grid of asterisks of size 3*3 in the next 3 lines diagonally. 
	- Similarly, the program must print the remaining grids of asterisks diagonally as the output. 
	- The program must print hyphens instead of empty spaces before each line. 
	
Boundary Condition(s): 
	1 <= N <= 25
Input Format: 
	The first line contains N. 
Output Format: 
	The first (N * (N+1))/2 lines contain the pattern based on the given conditions.
Example 
Input/Output 1:

Input: 
5 
Output: 
* 
- * * 
- * * 
- - - * * * 
- - - * * * 
- - - * * * 
- - - - - - * * * * 
- - - - - - * * * * 
- - - - - - * * * * 
- - - - - - * * * * 
- - - - - - - - - - * * * * * 
- - - - - - - - - - * * * * * 
- - - - - - - - - - * * * * * 
- - - - - - - - - - * * * * * 
- - - - - - - - - - * * * * * 

Explanation:
Here N = 5.
So 5 grids of asterisks are printed diagonally based on the given conditions. 

Example 
Input/Output 2:

Input: 
4 
Output: 
* 
- * * 
- * * 
- - - * * * 
- - - * * * 
- - - * * * 
- - - - - - * * * * 
- - - - - - * * * * 
- - - - - - * * * * 
- - - - - - * * * *

'''


n=int(input())
for i in range(n):
    for j in range(i+1):
        print(((i*(i+1))//2)*'- ',end='')
        print('* '*(i+1))



#end of program
