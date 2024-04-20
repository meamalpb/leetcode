class Solution:
    def productExceptSelf(self, nums):
        n=len(nums)
        lnum=[]
        rnum=[1]*n
        res=[]
        for i in range(n):
            if(i==0):
                lnum.append(nums[i])
                rnum[n-i-1]=(nums[n-i-1])
            else:
                lnum.append(lnum[i-1]*nums[i])
                rnum[n-i-1]=(rnum[n-i]*nums[n-i-1])
        for i in range(n):
            if(i==0):
                res.append(rnum[1])
            elif(i==(n-1)):
                res.append(lnum[n-2])
            else:
                res.append(lnum[i-1]*rnum[i+1])
        return res
sol=Solution()
print(sol.productExceptSelf([1,2,3,4]))