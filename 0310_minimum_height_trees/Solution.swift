// LeetCode 0310 - Minimum Height Trees
// https://leetcode.com/problems/minimum-height-trees/

class Solution {
    func findMinHeightTrees(_ n: Int, _ edges: [[Int]]) -> [Int] {
        if n <= 2 {
            return Array(0..<n)
        }

        var graph = Array(repeating: [Int](), count: n)
        var degree = Array(repeating: 0, count: n)
        for edge in edges {
            let left = edge[0]
            let right = edge[1]
            graph[left].append(right)
            graph[right].append(left)
            degree[left] += 1
            degree[right] += 1
        }

        var leaves = [Int]()
        for node in 0..<n where degree[node] == 1 {
            leaves.append(node)
        }

        var remaining = n
        while remaining > 2 {
            remaining -= leaves.count
            var newLeaves = [Int]()
            for leaf in leaves {
                for neighbor in graph[leaf] {
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1 {
                        newLeaves.append(neighbor)
                    }
                }
            }
            leaves = newLeaves
        }
        return leaves
    }
}
