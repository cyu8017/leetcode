// LeetCode 0547 - Number of Provinces
// https://leetcode.com/problems/number-of-provinces/

class Solution {
    func findCircleNum(_ isConnected: [[Int]]) -> Int {
        let n = isConnected.count
        var parent = Array(0..<n)

        func find(_ x: Int) -> Int {
            var node = x
            while parent[node] != node {
                parent[node] = parent[parent[node]]
                node = parent[node]
            }
            return node
        }

        func union(_ a: Int, _ b: Int) {
            let ra = find(a)
            let rb = find(b)
            if ra != rb {
                parent[rb] = ra
            }
        }

        for i in 0..<n {
            for j in (i + 1)..<n where isConnected[i][j] != 0 {
                union(i, j)
            }
        }

        var count = 0
        for i in 0..<n where find(i) == i {
            count += 1
        }
        return count
    }
}
