class Solution:
    def maxProfit(self, p):
        min1 = p[0]
        pr=0
        for i in p:
            if(i<min1):
                min1=i
            else:
                if(pr<(i-min1)):
                    pr=(i-min1)
        return pr

sol =Solution()
print(sol.maxProfit([7,1,5,3,6,4]))