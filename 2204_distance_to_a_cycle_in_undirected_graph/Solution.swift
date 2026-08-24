// LeetCode 2204 - Distance to a Cycle in Undirected Graph
// https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/

class Solution {
    func distanceToCycle(_ n: Int, _ edges: [[Int]]) -> [Int] {
        var g = [[Int]](repeating: [], count: n)
        var deg = [Int](repeating: 0, count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
            deg[e[0]] += 1
            deg[e[1]] += 1
        }
        var q: [Int] = []
        for i in 0..<n where deg[i] == 1 { q.append(i) }
        var onCycle = [Bool](repeating: true, count: n)
        var qi = 0
        while qi < q.count {
            let u = q[qi]; qi += 1
            onCycle[u] = false
            for v in g[u] {
                deg[v] -= 1
                if deg[v] == 1 { q.append(v) }
            }
        }
        var ans = [Int](repeating: -1, count: n)
        var qq: [Int] = []
        for i in 0..<n where onCycle[i] {
            ans[i] = 0
            qq.append(i)
        }
        qi = 0
        while qi < qq.count {
            let u = qq[qi]; qi += 1
            for v in g[u] where ans[v] == -1 {
                ans[v] = ans[u] + 1
                qq.append(v)
            }
        }
        return ans
    }
}
