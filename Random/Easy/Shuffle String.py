class Solution:
    def restoreString(self, s: str, i) -> str:
        n=len(s)
        t=["1"]*n
        for k,j in enumerate(i):
            t[j]=s[k]
        return "".join(t)
sol = Solution()
print(sol.restoreString("codeleet", [4,5,6,7,0,2,1,3]))