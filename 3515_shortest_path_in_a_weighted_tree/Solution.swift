// LeetCode 3515 - Shortest Path in a Weighted Tree
// https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

class Solution {
    var inT = [Int]()
    var outT = [Int]()
    var dist = [Int]()
    var parent = [Int]()
    var bit = [Int]()
    var time = 0
    var n = 0
    var g = [[[Int]]]()

    func dfs(_ u: Int, _ p: Int) {
        inT[u] = time
        time += 1
        for e in g[u] {
            let to = e[0], w = e[1]
            if to == p { continue }
            parent[to] = u
            dist[to] = dist[u] + w
            dfs(to, u)
        }
        outT[u] = time - 1
    }

    func add(_ i0: Int, _ v: Int) {
        var i = i0
        while i <= n {
            bit[i] += v
            i += i & -i
        }
    }

    func rangeAdd(_ l: Int, _ r: Int, _ v: Int) {
        add(l + 1, v)
        add(r + 2, -v)
    }

    func point(_ i0: Int) -> Int {
        var i = i0 + 1
        var s = 0
        while i > 0 {
            s += bit[i]
            i -= i & -i
        }
        return s
    }

    func treeQueries(_ n: Int, _ edges: [[Int]], _ queries: [[Int]]) -> [Int] {
        self.n = n
        g = Array(repeating: [], count: n + 1)
        var weight = [Int: Int]()
        for e in edges {
            let u = e[0], v = e[1], w = e[2]
            g[u].append([v, w])
            g[v].append([u, w])
            let a = min(u, v), b = max(u, v)
            weight[(a << 32) | b] = w
        }
        inT = Array(repeating: 0, count: n + 1)
        outT = Array(repeating: 0, count: n + 1)
        dist = Array(repeating: 0, count: n + 1)
        parent = Array(repeating: 0, count: n + 1)
        time = 0
        dfs(1, 0)
        bit = Array(repeating: 0, count: n + 2)
        for i in 1...n { rangeAdd(inT[i], inT[i], dist[i]) }
        var ans = [Int]()
        for q in queries {
            if q[0] == 1 {
                let u = q[1], v = q[2], nw = q[3]
                let a = min(u, v), b = max(u, v)
                let key = (a << 32) | b
                let ow = weight[key]!
                let delta = nw - ow
                weight[key] = nw
                let child = parent[u] == v ? u : v
                rangeAdd(inT[child], outT[child], delta)
            } else {
                ans.append(point(inT[q[1]]))
            }
        }
        return ans
    }
}
