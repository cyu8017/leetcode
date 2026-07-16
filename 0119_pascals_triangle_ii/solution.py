from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[1]
        for i in range(1, rowIndex+1): row.append(1); [row.__setitem__(j, row[j]+row[j-1]) for j in range(i-1, 0, -1)]
        return row
