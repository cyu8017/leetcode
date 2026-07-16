class Solution:
    def trimMean(self, arr):
        arr.sort(); k = len(arr) // 20
        return sum(arr[k:len(arr)-k]) / (len(arr) - 2*k)
