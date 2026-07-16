class Solution:
    def canFormArray(self, arr, pieces):
        by_first={p[0]:p for p in pieces}
        i=0
        while i<len(arr):
            if arr[i] not in by_first: return False
            p=by_first[arr[i]]
            if arr[i:i+len(p)]!=p: return False
            i+=len(p)
        return True
