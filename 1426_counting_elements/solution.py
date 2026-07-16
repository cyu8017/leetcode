class Solution:
    def countElements(self, arr):
        values = set(arr)
        return sum(value + 1 in values for value in arr)
