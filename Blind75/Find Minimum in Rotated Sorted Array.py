class Solution:
    def findMin(self, nums) -> int:
        l,r=0,len(nums)-1
        while(l<=r):
            m=(l+r)//2
            if(nums[l]<nums[m]):
                if(nums[r]<nums[m]):
                    l+=1
                else:
                    r-=1
            else:
                if(nums[r]<nums[m]):
                    l+=1
                else:
                    r-=1
        return nums[l]



    
sol=Solution()
print(sol.findMin([4,5,6,7,0,1,2]))