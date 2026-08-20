// LeetCode 1319 - Number of Operations to Make Network Connected
// https://leetcode.com/problems/number-of-operations-to-make-network-connected/

class Solution {
    func makeConnected(_ n: Int, _ connections: [[Int]]) -> Int {
        if connections.count < n - 1 { return -1 }
        var parent = Array(0..<n)
        func find(_ x: Int) -> Int {
            if parent[x] != x { parent[x] = find(parent[x]) }
            return parent[x]
        }
        var components = n
        for e in connections {
            let a = find(e[0]), b = find(e[1])
            if a != b { parent[a] = b; components -= 1 }
        }
        return components - 1
    }
}
