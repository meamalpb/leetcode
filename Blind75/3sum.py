class Solution:
    def threeSum(self, nums):
            nums.sort()
            k=set()
            n=len(nums)
            for i,j in enumerate(nums):
                if(j>0):
                    break
                if(i>n-2 or (i!=0 and j==nums[i-1])):
                    continue
                else:
                    l,r=i+1,n-1
                    while(l<r):
                        d=j+nums[l]+nums[r]
                        if(d==0):
                            k.add((j,nums[l],nums[r]))
                            l+=1
                            r-=1
                        elif(d>0):
                            r-=1
                        else:
                            l+=1
            return k
    
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))