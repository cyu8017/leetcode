// LeetCode 3820 - Pythagorean Distance Nodes In A Tree
// https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/

class Solution {
    private var g = [[Int]]()
    private var n = 0

    func specialNodes(_ n: Int, _ edges: [[Int]], _ x: Int, _ y: Int, _ z: Int) -> Int {
        self.n = n
        g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        let d1 = bfs(x), d2 = bfs(y), d3 = bfs(z)
        var ans = 0
        for i in 0..<n {
            var a = [d1[i], d2[i], d3[i]]
            a.sort()
            if a[0] * a[0] + a[1] * a[1] == a[2] * a[2] { ans += 1 }
        }
        return ans
    }

    private func bfs(_ start: Int) -> [Int] {
        var dist = [Int](repeating: 1_000_000_000, count: n)
        var q = [start]
        dist[start] = 0
        var head = 0
        while head < q.count {
            let u = q[head]
            head += 1
            for v in g[u] {
                if dist[v] > dist[u] + 1 {
                    dist[v] = dist[u] + 1
                    q.append(v)
                }
            }
        }
        return dist
    }
}
