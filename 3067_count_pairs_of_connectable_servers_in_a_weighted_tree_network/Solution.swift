// LeetCode 3067 - Count Pairs of Connectable Servers in a Weighted Tree Network
// https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

class Solution {
    func countPairsOfConnectableServers(_ edges: [[Int]], _ signalSpeed: Int) -> [Int] {
        let n = edges.count + 1
        var g = Array(repeating: [(Int, Int)](), count: n)
        for e in edges {
            g[e[0]].append((e[1], e[2]))
            g[e[1]].append((e[0], e[2]))
        }

        func dfs(_ a: Int, _ fa: Int, _ ws: Int) -> Int {
            var cnt = ws % signalSpeed == 0 ? 1 : 0
            for (b, w) in g[a] where b != fa {
                cnt += dfs(b, a, ws + w)
            }
            return cnt
        }

        var ans = Array(repeating: 0, count: n)
        for a in 0..<n {
            var s = 0
            for (b, w) in g[a] {
                let t = dfs(b, a, w)
                ans[a] += s * t
                s += t
            }
        }
        return ans
    }
}
