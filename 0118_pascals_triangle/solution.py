from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        for i in range(numRows): result.append([1 if j == 0 or j == i else result[-1][j-1]+result[-1][j] for j in range(i+1)])
        return result
