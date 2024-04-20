class Solution:
    def maxProduct(self, nums) -> int:
        maxp=minp=res=nums[0]
        for i in range(1,len(nums)):
            tmax = max(nums[i]*maxp,nums[i]*minp,nums[i])
            tmin = min(nums[i]*maxp,nums[i]*minp,nums[i])
            print(tmax,tmin,nums[i])
            maxp,minp=tmax,tmin
            res=max(maxp,res)

        return res
    
sol=Solution()
print(sol.maxProduct([2,3,-2,4]))