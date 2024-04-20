class Solution:
    def maxArea(self, h) -> int:
        l,r=0,len(h)-1
        maxp=0
        while(l<r):
            if(h[l]>h[r]):
                curr=h[r]*(r-l)
                r-=1
            else:
                curr=h[l]*(r-l)
                l+=1
            if(maxp<curr):
                maxp=curr
        return maxp
sol=Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))