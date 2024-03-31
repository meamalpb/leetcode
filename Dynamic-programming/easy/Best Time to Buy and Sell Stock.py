class Solution:
    def maxProfit(self, p):
        minPrice = p[0]
        pr=0
        for i in p:
            if(i<minPrice):
                minPrice=i
            else:
                if(pr<(i-minPrice)):
                    pr=i-minPrice
        return pr
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))