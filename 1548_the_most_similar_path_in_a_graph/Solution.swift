// LeetCode 1548 - The Most Similar Path in a Graph
// https://leetcode.com/problems/the-most-similar-path-in-a-graph/

class Solution {
    func mostSimilar(_ n: Int, _ roads: [[Int]], _ names: [String], _ targetPath: [String]) -> [Int] {
        var graph = Array(repeating: [Int](), count: n)
        for r in roads {
            graph[r[0]].append(r[1])
            graph[r[1]].append(r[0])
        }
        var dp: [(cost: Int, path: [Int])] = (0..<n).map { node in
            (names[node] == targetPath[0] ? 0 : 1, [node])
        }
        for i in 1..<targetPath.count {
            var nextDp = [(cost: Int, path: [Int])]()
            for node in 0..<n {
                var bestCost = Int.max
                var bestPath = [Int]()
                for prev in graph[node] {
                    if dp[prev].cost < bestCost {
                        bestCost = dp[prev].cost
                        bestPath = dp[prev].path
                    }
                }
                nextDp.append((bestCost + (names[node] == targetPath[i] ? 0 : 1), bestPath + [node]))
            }
            dp = nextDp
        }
        return dp.min(by: { $0.cost < $1.cost })!.path
    }
}
