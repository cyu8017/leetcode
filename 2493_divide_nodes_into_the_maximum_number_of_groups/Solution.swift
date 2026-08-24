// LeetCode 2493 - Divide Nodes Into the Maximum Number of Groups
// https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

class Solution {
    func magnificentSets(_ n: Int, _ edges: [[Int]]) -> Int {
        var g = [[Int]](repeating: [], count: n + 1)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        func bfsDepth(_ start: Int) -> Int {
            var dist = [Int](repeating: -1, count: n + 1)
            var q = [start]
            dist[start] = 1
            var best = 1
            var i = 0
            while i < q.count {
                let u = q[i]; i += 1
                best = max(best, dist[u])
                for v in g[u] where dist[v] == -1 {
                    dist[v] = dist[u] + 1
                    q.append(v)
                }
            }
            return best
        }
        var color = [Int](repeating: -1, count: n + 1)
        var components = [[Int]]()
        for i in 1...n {
            if color[i] != -1 { continue }
            var comp = [Int]()
            var q = [i]
            color[i] = 0
            var bipartite = true
            var qi = 0
            while qi < q.count {
                let u = q[qi]; qi += 1
                comp.append(u)
                for v in g[u] {
                    if color[v] == -1 {
                        color[v] = color[u] ^ 1
                        q.append(v)
                    } else if color[v] == color[u] {
                        bipartite = false
                    }
                }
            }
            if !bipartite { return -1 }
            components.append(comp)
        }
        var ans = 0
        for comp in components {
            var best = 0
            for u in comp { best = max(best, bfsDepth(u)) }
            ans += best
        }
        return ans
    }
}
