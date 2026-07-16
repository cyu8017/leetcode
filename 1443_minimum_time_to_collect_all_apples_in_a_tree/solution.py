class Solution:
    def minTime(self, n, edges, hasApple):
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        def visit(node, parent):
            cost = 0
            for child in graph[node]:
                if child != parent:
                    child_cost = visit(child, node)
                    if child_cost or hasApple[child]:
                        cost += child_cost + 2
            return cost
        return visit(0, -1)
