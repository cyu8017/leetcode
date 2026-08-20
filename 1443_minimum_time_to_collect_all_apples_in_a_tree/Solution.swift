// LeetCode 1443 - Minimum Time to Collect All Apples in a Tree
// https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

class Solution {
    func minTime(_ n: Int, _ edges: [[Int]], _ hasApple: [Bool]) -> Int {
        var graph = Array(repeating: [Int](), count: n)
        for e in edges { graph[e[0]].append(e[1]); graph[e[1]].append(e[0]) }
        func visit(_ node: Int, _ parent: Int) -> Int {
            var cost = 0
            for child in graph[node] where child != parent {
                let childCost = visit(child, node)
                if childCost > 0 || hasApple[child] { cost += childCost + 2 }
            }
            return cost
        }
        return visit(0, -1)
    }
}
