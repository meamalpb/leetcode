class Solution:
    def generate(self, n: int):
        k=[]
        for i in range(n):
            k.append([1]*(i+1))
            for j in range(1,i):
                k[i][j]=k[i][i-j]=k[i-1][j-1]+k[i-1][j]
        return k 
sol =  Solution()
print(sol.generate(8))


# [1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]
