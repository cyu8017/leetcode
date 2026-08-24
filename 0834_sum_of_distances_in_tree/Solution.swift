// LeetCode 0834 - Sum of Distances in Tree
// https://leetcode.com/problems/sum-of-distances-in-tree/

class Solution {
    func sumOfDistancesInTree(_ n: Int, _ edges: [[Int]]) -> [Int] {
        var graph = Array(repeating: [Int](), count: n)
        for e in edges {
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        }
        var count = Array(repeating: 1, count: n)
        var ans = Array(repeating: 0, count: n)
        func post(_ node: Int, _ parent: Int) {
            for child in graph[node] where child != parent {
                post(child, node)
                count[node] += count[child]
                ans[node] += ans[child] + count[child]
            }
        }
        func reroot(_ node: Int, _ parent: Int) {
            for child in graph[node] where child != parent {
                ans[child] = ans[node] - count[child] + (n - count[child])
                reroot(child, node)
            }
        }
        post(0, -1)
        reroot(0, -1)
        return ans
    }
}
