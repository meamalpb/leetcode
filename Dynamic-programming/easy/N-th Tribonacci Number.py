class Solution:
    def fib(self, n: int) -> int:
        r=[0,1,1]
        for i in range(3,n+1):
            r.append(r[i-1]+r[i-2]+r[i-3])
        return r[n]
sol= Solution()
print(sol.fib(25))