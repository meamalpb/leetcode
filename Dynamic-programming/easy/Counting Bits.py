class Solution:
    def countBits(self, n: int) :
        k=1
        dp=[0]*(n+1)
        for i in range(1,n+1):
            if(i==k*2):
                k*=2
            dp[i]=1+dp[i-k]
        return dp
sol = Solution()
print(sol.countBits(8))