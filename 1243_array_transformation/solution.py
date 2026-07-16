class Solution:
    def transformArray(self, arr: list[int]) -> list[int]:
        while True:
            nxt = arr[:]
            for i in range(1, len(arr) - 1):
                if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]: nxt[i] += 1
                elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]: nxt[i] -= 1
            if nxt == arr: return arr
            arr = nxt
