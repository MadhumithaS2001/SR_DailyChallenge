'''

Triangle Pattern with Integer Series

The program must accept an integer N as the input.
The program must form a string S by concatenating the positive integers from 1.
Then the program must print the N lines of the pattern based on the following conditions. 
  - In the 1st line, N-1 asterisks and the first character in the string S. 
  - In the 2nd line, N-2 asterisks and the next 3 characters in the string S. 
  - In the 3rd line, N-3 asterisks and the next 5 characters in the string S. 
  - In the 4th line, N-4 asterisks and the next 7 characters in the string S. 
  - Similarly, the program must print the remaining lines of the pattern as the output.

Boundary Condition(s):

3 <= N <= 100 

Input Format: 

The first line contain N. 

Output Format:

The first N lines contain the pattern based on the given conditions. 

Example 
Input/Output 1: 

Input: 

5 

Output: 

****1
***234
**56789
*1011121
314151617

Explanation: 

Here N = 5, so the pattern contains 5 lines.
The string S is formed as 1234567891011121314151617181920212223... and so on.
So the 5 lines of pattern are printed based on the given conditions.

Example 
Input/Output 2:

Input: 

8 

Output: 

*******1
******234
*****56789
****1011121
***314151617
**18192021222
*3242526272829
303132333435363


'''

n = int(input())
x = 1
l = ''
y=1
for i in range(1, n * n):
    l += str(i)
for i in range(1, n + 1):
    print('*' * (n - i), end='')
    if (i == 1):
        print(l[0], end='')
    else:
        y += 2
        print(l[x:x+y], end='')
        x+=y
    print()

    
#end
