# LeetCode 1519

class Solution:
    def countSubTrees(self, n, edges, labels):
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        answer = [0] * n
        def dfs(node, parent):
            counts = [0] * 26
            index = ord(labels[node]) - 97
            counts[index] = 1
            for neighbor in graph[node]:
                if neighbor != parent:
                    child = dfs(neighbor, node)
                    for i in range(26):
                        counts[i] += child[i]
            answer[node] = counts[index]
            return counts
        dfs(0, -1)
        return answer
