// LeetCode 2603 - Collect Coins in a Tree
// https://leetcode.com/problems/collect-coins-in-a-tree/

class Solution {
    func collectTheCoins(_ coins: [Int], _ edges: [[Int]]) -> Int {
        let n = coins.count
        var g = [Set<Int>](repeating: Set<Int>(), count: n)
        for e in edges {
            g[e[0]].insert(e[1])
            g[e[1]].insert(e[0])
        }
        var deg = g.map { $0.count }
        var q = [Int]()
        for i in 0..<n where deg[i] == 1 && coins[i] == 0 { q.append(i) }
        var qi = 0
        while qi < q.count {
            let u = q[qi]; qi += 1
            for v in g[u] {
                g[v].remove(u)
                deg[v] -= 1
                if deg[v] == 1 && coins[v] == 0 { q.append(v) }
            }
            g[u].removeAll()
            deg[u] = 0
        }
        for _ in 0..<2 {
            var leaves = [Int]()
            for i in 0..<n where deg[i] == 1 { leaves.append(i) }
            for u in leaves {
                for v in g[u] {
                    g[v].remove(u)
                    deg[v] -= 1
                }
                g[u].removeAll()
                deg[u] = 0
            }
        }
        return g.reduce(0) { $0 + $1.count }
    }
}
