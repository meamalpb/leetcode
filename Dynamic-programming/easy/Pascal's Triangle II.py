class Solution:
    def getRow(self, r: int):
        k=[[1]]
        for i in range(1,r+1):
            k.append([1]*(i+1))
            for j in range(1,i):
                k[i][j]=k[i][i-j]=k[i-1][j-1]+k[i-1][j]
        return k[r]
    
sol = Solution()
print(sol.getRow(0))