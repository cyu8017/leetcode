// LeetCode 3313 - Find the Last Marked Nodes in Tree
// https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

class Solution {
    func lastMarkedNodes(_ edges: [[Int]]) -> [Int] {
        let n = edges.count + 1
        var g = Array(repeating: [Int](), count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        func bfs(_ start: Int) -> (Int, [Int]) {
            var dist = Array(repeating: -1, count: n)
            var q = [start]
            dist[start] = 0
            var far = start
            var qi = 0
            while qi < q.count {
                let u = q[qi]; qi += 1
                if dist[u] > dist[far] { far = u }
                for v in g[u] where dist[v] == -1 {
                    dist[v] = dist[u] + 1
                    q.append(v)
                }
            }
            return (far, dist)
        }
        let u = bfs(0).0
        let (v, du) = bfs(u)
        let dv = bfs(v).1
        var ans = Array(repeating: 0, count: n)
        for i in 0..<n { ans[i] = du[i] >= dv[i] ? u : v }
        return ans
    }
}
