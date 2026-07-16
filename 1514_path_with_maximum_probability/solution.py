# LeetCode 1514

class Solution:
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        import heapq
        graph = [[] for _ in range(n)]
        for (a, b), probability in zip(edges, succProb):
            graph[a].append((b, probability))
            graph[b].append((a, probability))
        heap = [(-1.0, start_node)]
        best = [0.0] * n
        best[start_node] = 1.0
        while heap:
            probability, node = heapq.heappop(heap)
            probability = -probability
            if node == end_node:
                return probability
            if probability < best[node]:
                continue
            for neighbor, edge_probability in graph[node]:
                candidate = probability * edge_probability
                if candidate > best[neighbor]:
                    best[neighbor] = candidate
                    heapq.heappush(heap, (-candidate, neighbor))
        return 0.0
