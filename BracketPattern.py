'''

The program must accept an integer N within a pair of brackets as the input. 
The pair of brackets can be any one of the following four types. 
1) Parentheses() 
2) Square brackets[] 
3) Curly brackets{} 
4) Angle brackets<> 
The program must print the given brackets in N lines based on the following conditions. 
	- In the 1st line, only one pair of brackets must be printed. 
	- In the 2nd line, 2nd level nested brackets and one pair of brackets must be printed. 
	- In the 3rd line, 3rd level, 2nd level nested brackets and one pair of brackets must be printed. 
	- In the 4th line, 4th level, 3rd level, 2nd level nested brackets and one pair of brackets must be printed. 
	- Similarly, the remaining lines must be printed as the output. 
Boundary Condition(s): 
	1 <= N <= 25 
Input Format: 
	The first line contains N within a pair of brackets. 
Output Format: 
	The first N lines contain the brackets pattern based on the given conditions.
Example Input/Output 1:
	Input: (4) 
	Output: () 
			(())() 
			((()))(())() 
			(((())))((()))(())() 
	Explanation: 
		Here N = 4 and the type of the brackets is Parentheses().
		So the parentheses are printed in 4 lines based on the given conditions.
Example Input/Output 2:
	Input: [5] 
	Output: [] 
			[[]][] 
			[[[]]][[]][] 
			[[[[]]]][[[]]][[]][] 
			[[[[[]]]]][[[[]]]][[[]]][[]][] 
Example Input/Output 3: 
	Input: {6} 
	Output: {} 
			{{}}{} 
			{{{}}}{{}}{} 
			{{{{}}}}{{{}}}{{}}{} 
			{{{{{}}}}}{{{{}}}}{{{}}}{{}}{}
			{{{{{{}}}}}}{{{{{}}}}}{{{{}}}}{{{}}}{{}}{} 
Example Input/Output 4: 
	Input: <3> 
	Output: <> 
			<<>><> 
			<<<>>><<>><>
		
'''		
		
s=input().strip()
c1=s[0]
n=int(s[1:-1])
c2=s[-1]
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(c1*j+c2*j,end='')
    print()
	
	
	
	
#end	
