'''
Swap Every Two Vowels 
 The program must accept a string S as the input. The program must swap every two vowels in the string S. Then the program must print the revised string S as the output. If the number of vowels is odd, then the last vowel will remain the same as there is no pair to swap.

Note: The string S always contains at least two vowels.

Input Format:

The first line contains S.

Output Format:

The first line contains the revised string S.

Example Input/Output 1:

Input:

environment

Output:

inverenmont

Explanation:

There are four vowels in the given string "environment".

After swapping the vowels e and i, the string environment becomes inveronment.

After swapping the vowels o and e, the string inveronment becomes inverenmont.

Hence the output is inverenmont.

Example Input/Output 2:

Input:

TOUCHPAD

Output:

TUOCHPAD
'''


s=list(input().strip())
v=[-1,-1]
for i in range(len(s)):
    if(s[i] in "aeiouAEIOU"):
        if(v[0]==-1):
            v[0]=i
        elif(v[1]==-1):
            v[1]=i
    if(v[0]!=1 and v[1]!=-1):
        s[v[0]],s[v[1]]=s[v[1]],s[v[0]]
        v[0],v[1]=-1,-1
print(''.join(s))



