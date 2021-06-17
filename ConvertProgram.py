'''
Convert this C Program to Python Program :

int N; 
scanf("%d", &N); 
char numStr[10]; 
int len = sprintf(numStr, "%d", N); 
int sum = 0, currVal; 
	for(int index = len-1; index >= 0; index--) 
	{ 
		if(numStr[index] != '0') 
		{ 
			sscanf(numStr+index, "%d", &currVal); 
			sum += currVal; 
		} 
	} 
printf("%d", sum);
return 0; 
}


input:   
1234

output:
1506

explanation:
4 + 34 + 234 + 1234


input:   
9807

output:
10621

explanation:
7 + _ + 807 + 9087


'''

n=input()
s=0
for i in range(len(n)-1,-1,-1):
    if(n[i] != '0'):
        s+=int(n[i:])
print(s)









#End
