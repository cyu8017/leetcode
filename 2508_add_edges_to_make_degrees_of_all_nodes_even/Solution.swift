// LeetCode 2508 - Add Edges to Make Degrees of All Nodes Even
// https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

class Solution {
    func isPossible(_ n: Int, _ edges: [[Int]]) -> Bool {
        var deg = [Int](repeating: 0, count: n + 1)
        var adj = [Set<Int>](repeating: Set<Int>(), count: n + 1)
        for e in edges {
            let u = e[0], v = e[1]
            deg[u] += 1
            deg[v] += 1
            adj[u].insert(v)
            adj[v].insert(u)
        }
        var odd = [Int]()
        for i in 1...n where deg[i] % 2 == 1 { odd.append(i) }
        if odd.isEmpty { return true }
        if odd.count == 2 {
            let a = odd[0], b = odd[1]
            if !adj[a].contains(b) { return true }
            for i in 1...n {
                if i != a && i != b && !adj[a].contains(i) && !adj[b].contains(i) { return true }
            }
            return false
        }
        if odd.count == 4 {
            let a = odd[0], b = odd[1], c = odd[2], d = odd[3]
            return (!adj[a].contains(b) && !adj[c].contains(d))
                || (!adj[a].contains(c) && !adj[b].contains(d))
                || (!adj[a].contains(d) && !adj[b].contains(c))
        }
        return false
    }
}
