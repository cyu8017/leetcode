// LeetCode 3787 - Find Diameter Endpoints Of A Tree
// https://leetcode.com/problems/find-diameter-endpoints-of-a-tree/

class Solution {
    private var g = [[Int]]()
    private var n = 0

    func findSpecialNodes(_ n: Int, _ edges: [[Int]]) -> String {
        self.n = n
        g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        let r0 = bfs(0)
        let a = r0.0
        let r1 = bfs(a)
        let b = r1.0
        let dist1 = r1.1
        let r2 = bfs(b)
        let dist2 = r2.1
        let d = dist1[b]
        var ans = [Character](repeating: "0", count: n)
        for i in 0..<n {
            if dist1[i] == d || dist2[i] == d { ans[i] = "1" }
        }
        return String(ans)
    }

    private func bfs(_ start: Int) -> (Int, [Int]) {
        var dist = [Int](repeating: -1, count: n)
        dist[start] = 0
        var q = [start]
        var far = start
        var head = 0
        while head < q.count {
            let u = q[head]
            head += 1
            if dist[u] > dist[far] { far = u }
            for v in g[u] {
                if dist[v] == -1 {
                    dist[v] = dist[u] + 1
                    q.append(v)
                }
            }
        }
        return (far, dist)
    }
}
