// LeetCode 3342 - Find Minimum Time to Reach Last Room II
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/

private struct MinHeap4 {
    private var a: [(Int, Int, Int, Int)] = []
    var isEmpty: Bool { a.isEmpty }
    mutating func push(_ x: (Int, Int, Int, Int)) {
        a.append(x)
        var i = a.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if a[p].0 <= a[i].0 { break }
            a.swapAt(p, i)
            i = p
        }
    }
    mutating func pop() -> (Int, Int, Int, Int) {
        let r = a[0]
        let last = a.removeLast()
        if !a.isEmpty {
            a[0] = last
            var i = 0
            while true {
                var s = i
                let l = 2 * i + 1, rg = 2 * i + 2
                if l < a.count && a[l].0 < a[s].0 { s = l }
                if rg < a.count && a[rg].0 < a[s].0 { s = rg }
                if s == i { break }
                a.swapAt(i, s)
                i = s
            }
        }
        return r
    }
}

class Solution {
    func minTimeToReach(_ moveTime: [[Int]]) -> Int {
        let m = moveTime.count, n = moveTime[0].count
        let INF = 1 << 30
        var dist = Array(repeating: Array(repeating: Array(repeating: INF, count: 2), count: n), count: m)
        var pq = MinHeap4()
        dist[0][0][0] = 0
        pq.push((0, 0, 0, 0))
        let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while !pq.isEmpty {
            let (t, r, c, parity) = pq.pop()
            if t != dist[r][c][parity] { continue }
            if r == m - 1 && c == n - 1 { return t }
            let cost = parity == 1 ? 2 : 1
            for (dr, dc) in dirs {
                let nr = r + dr, nc = c + dc
                if nr < 0 || nc < 0 || nr >= m || nc >= n { continue }
                let start = max(t, moveTime[nr][nc])
                let nt = start + cost
                let np = 1 - parity
                if nt < dist[nr][nc][np] {
                    dist[nr][nc][np] = nt
                    pq.push((nt, nr, nc, np))
                }
            }
        }
        return -1
    }
}
