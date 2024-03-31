class Solution:
    def fib(self, n: int) -> int:
        r=[0,1]
        for i in range(2,n+1):
            r.append(r[i-1]+r[i-2])
        return r[n]
sol= Solution()
print(sol.fib(8))