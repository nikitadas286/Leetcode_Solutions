class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        op=[]
        for i in digits:
            data=str(i)
            op.append(data)
        res= "".join(op)
        add=str(int(res)+1)
        arr=list(map(int,add))
        return arr
        