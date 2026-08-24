// LeetCode 3620 - Network Recovery Pathways
// https://leetcode.com/problems/network-recovery-pathways/

class Solution {
    var g = [[[Int]]]()
    var k = 0
    var n = 0

    func check(_ mid: Int) -> Bool {
        let INF = Int.max / 2
        var dist = Array(repeating: INF, count: n)
        dist[0] = 0
        var pq = [(0, 0)]
        while !pq.isEmpty {
            pq.sort { $0.0 < $1.0 }
            let cur = pq.removeFirst()
            let d = cur.0, u = cur.1
            if d > k { return false }
            if u == n - 1 { return true }
            if dist[u] < d { continue }
            for e in g[u] {
                let v = e[0], w = e[1]
                if w < mid { continue }
                let nd = d + w
                if nd < dist[v] {
                    dist[v] = nd
                    pq.append((nd, v))
                }
            }
        }
        return false
    }

    func findMaxPathScore(_ edges: [[Int]], _ online: [Bool], _ k: Int) -> Int {
        self.k = k
        n = online.count
        g = Array(repeating: [], count: n)
        var l = Int.max, r = 0
        for e in edges {
            let u = e[0], v = e[1], w = e[2]
            if !online[u] || !online[v] { continue }
            g[u].append([v, w])
            l = min(l, w)
            r = max(r, w)
        }
        if l == Int.max { return -1 }
        while l < r {
            let mid = (l + r + 1) >> 1
            if check(mid) { l = mid } else { r = mid - 1 }
        }
        return check(l) ? l : -1
    }
}
