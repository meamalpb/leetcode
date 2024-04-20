class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        k=[]
        i,j=0,0
        while(i<len(word1) and j<len(word2)):
            k.append(word1[i])
            k.append(word2[j])
            i+=1
            j+=1
        while(i<len(word1)):
            k.append(word1[i])
            i+=1
        while(j<len(word2)):
            k.append(word2[j])
            j+=1
        return "".join(k)
sol = Solution()
print(sol.mergeAlternately("abc","pqrs"))