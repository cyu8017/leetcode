class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        import heapq
        heap = []
        for p, t in classes:
            gain = (p + 1) / (t + 1) - p / t
            heapq.heappush(heap, (-gain, p, t))
        for _ in range(extraStudents):
            _, p, t = heapq.heappop(heap)
            p += 1; t += 1
            gain = (p + 1) / (t + 1) - p / t
            heapq.heappush(heap, (-gain, p, t))
        return sum(p / t for _, p, t in heap) / len(heap)
