class Solution:
    def search(self, nums, t: int) -> int:
        l,r=0,len(nums)-1
        while(l<=r):
            m=(l+r)//2
            if(nums[m]==t):
                return m
            if(nums[l]<=nums[m]):
                if(nums[l]>t or nums[m]<t):
                    l=m+1
                else:
                    r=m-1
            else:
                if(nums[r]>t or nums[m]>t):
                    r=m-1
                else:
                    l=m+1
        return -1
                
sol=Solution()
print(sol.search([4,5,6,7,0,1,2],2))