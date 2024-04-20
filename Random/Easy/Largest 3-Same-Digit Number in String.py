class Solution:
    def largestGoodInteger(self, num: str) -> str:
        k=[]
        for i in range(9,-1,-1):
            k.append(str(i)*3)
        for i in k:
            if(i in num):
                return i
        return ""
            
        
sol = Solution()
print(sol.largestGoodInteger("6777133339"))