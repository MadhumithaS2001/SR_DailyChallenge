/*
Pattern Reverse

Input:

5

Output:

54321
4321
321
21
1
12
123
1234
12345
*/
void printPattern(int N){
	int j,i;
	for(i=N;i>0;i--){
		for(j=i;j>0;j--){
			printf("%d",j);
		}
		printf("\n");
	}
	for(i=1;i<N;i++){
		for(j=1;j<=i+1;j++){
			printf("%d",j);
		}
		printf("\n");
	}
}
int main(){
	int n;
	scanf("%d",&n);
	printPattern(n);
}	




//end of program
