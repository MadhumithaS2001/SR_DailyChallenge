'''
Input:

4 3

4 5 6
7 8 9
1 2 3
0 11 12 

9 3 12
6 8 11
5 2 0
4 7 1

Output: 

YES

'''
r, c = map(int, input().split())
m1 = []
m2 = []
for i in range(r):
    m1.append(list(map(int, input().split())))
for i in range(r):
    m2.append(list(map(int, input().split())))

l = []

l += m1[0]

for i in range(1, r-1):
    l.append(m1[i][c - 1])
l += m1[r-1][::-1]

for i in range(r - 2, 0, -1):
    l.append(m1[i][0])

l2 = []
l2 += m2[0]
for i in range(1, r-1):
    l2.append(m2[i][c - 1])
l2 += m2[r - 1][::-1]
for i in range(r - 2, 0, -1):
    l2.append(m2[i][0])

first = l[0]
ind = l2.index(first)
l2 = l2[ind:] + l2[:ind]

print("YES" if(l==l2) else "NO")
