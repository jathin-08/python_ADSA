from typing import List

'''
2D : The data can be store in the form of rows & Column 
"Matrx"
Ex:
a = [[1,2,3],[4,5,6],[7,8,9]]

    0   1   2
0   1   2   3
   
1   4   5   6
 
2   7   8   9 

a[0][0] = 1
a[0][1] = 2
------------
------------
------------

'''
#Leet Code : 1572
'''
n = len(mat)
total = 0
for i in range(n):
    for j in range(n):    #Time Complexity -->O(n**2)
        if (i==j):
            total1 += mat[i][j]
        elif (i+j == n -1):
            total2 += mat[i][j]
        total = total1 + total2
    if n % 2 ==1:
        total -= mat[n//2][n//2]
return total
'''

class Solution1572:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i]
            total += mat[i][n-1-i]
            if n % 2 ==1:
                total -= mat[n//2][n//2]   #mat[1][1]
        return total

#Leet Code : 498
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        result = []

        for d in range(rows + cols - 1):
            dia = []
            r = 0 if d < cols else d-cols+1
            c = d if d < cols else cols-1
            while r < rows and c >=0:
                dia.append(mat[r][c])
                r += 1
                c -=1
            if d % 2 == 0:
                dia.reverse()
            result.extend(dia)
        return result
