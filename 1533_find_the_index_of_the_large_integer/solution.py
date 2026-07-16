# LeetCode 1533

class ArrayReader:
    def __init__(self, arr):
        self.arr = arr
    def compareSub(self, l, r, x, y):
        a, b = sum(self.arr[l:r + 1]), sum(self.arr[x:y + 1])
        return (a > b) - (a < b)
    def length(self):
        return len(self.arr)

class Solution:
    def getIndex(self, reader):
        if isinstance(reader, list):
            reader = ArrayReader(reader)
        left, right = 0, reader.length() - 1
        while left < right:
            length = right - left + 1
            half = length // 2
            result = reader.compareSub(left, left + half - 1, right - half + 1, right)
            if result == 0:
                return left + half
            if result > 0:
                right = left + half - 1
            else:
                left = right - half + 1
        return left
