class Solution:
    def containsDuplicate(self, nums) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        
        return False

sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))