class Solution:
    def findMin(self, nums) -> int:
        left, right = 0, len(nums) - 1
        if(nums[left]<nums[right]): return nums[left]
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[right]



    
sol=Solution()
print(sol.findMin([4,5,6,7,0,1,2]))