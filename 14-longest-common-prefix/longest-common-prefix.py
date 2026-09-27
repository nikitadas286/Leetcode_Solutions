class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        op=""
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                op+= chars[0]
            else:
                break
        return op


                