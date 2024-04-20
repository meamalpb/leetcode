class Solution:
    def maxSubArray(self, nums) -> int:
        res=nums[0]
        currmax = nums[0]
        for i in range(1,len(nums)):
            if (currmax+nums[i]<nums[i]):
                print(currmax,nums[i])
                currmax = nums[i]
            else:
                currmax = currmax+nums[i]
            if(currmax>res):
                res=currmax
        return res
sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))