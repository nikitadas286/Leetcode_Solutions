class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str1=s.strip()
        li=str1.split(" ")
        return (len(li[-1]))