// LeetCode 1719 - Number Of Ways To Reconstruct A Tree
// https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

class Solution {
    func checkWays(_ pairs: [[Int]]) -> Int {
        var graph = [Int: Set<Int>]()
        for pair in pairs {
            graph[pair[0], default: []].insert(pair[1])
            graph[pair[1], default: []].insert(pair[0])
        }
        let n = graph.count
        var root: Int? = nil
        for (node, neighbors) in graph where neighbors.count == n - 1 {
            root = node
            break
        }
        guard let rootNode = root else {
            return 0
        }
        var ans = 1
        for (node, neighbors) in graph {
            if node == rootNode {
                continue
            }
            var parent: Int? = nil
            var parentDegree = n + 1
            for nei in neighbors {
                let neiDegree = graph[nei]!.count
                if neiDegree >= neighbors.count && neiDegree < parentDegree {
                    parent = nei
                    parentDegree = neiDegree
                }
            }
            guard let parentNode = parent else {
                return 0
            }
            for nei in neighbors {
                if nei != parentNode && !graph[parentNode]!.contains(nei) {
                    return 0
                }
            }
            if graph[parentNode]!.count == neighbors.count {
                ans = 2
            }
        }
        return ans
    }
}
