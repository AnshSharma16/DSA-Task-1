class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return s
            s += strs[0][i]
        return s
        
