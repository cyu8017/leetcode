import heapq

class Solution:
    def kthSmallest(self, mat, k):
        sums = [0]
        for row in mat:
            heap = [(sums[0] + row[0], 0, 0)]
            merged = []
            while heap and len(merged) < k:
                value, i, j = heapq.heappop(heap)
                merged.append(value)
                if j + 1 < len(row):
                    heapq.heappush(heap, (sums[i] + row[j + 1], i, j + 1))
                if j == 0 and i + 1 < len(sums):
                    heapq.heappush(heap, (sums[i + 1] + row[0], i + 1, 0))
            sums = merged
        return sums[k - 1]
