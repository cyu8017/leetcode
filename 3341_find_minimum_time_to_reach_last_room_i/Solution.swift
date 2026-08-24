// LeetCode 3341 - Find Minimum Time to Reach Last Room I
// https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/

private struct MinHeap3 {
    private var a: [(Int, Int, Int)] = []
    var isEmpty: Bool { a.isEmpty }
    mutating func push(_ x: (Int, Int, Int)) {
        a.append(x)
        var i = a.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if a[p].0 <= a[i].0 { break }
            a.swapAt(p, i)
            i = p
        }
    }
    mutating func pop() -> (Int, Int, Int) {
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
        var dist = Array(repeating: Array(repeating: 1 << 30, count: n), count: m)
        var h = MinHeap3()
        h.push((0, 0, 0))
        dist[0][0] = 0
        let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while !h.isEmpty {
            let (t, r, c) = h.pop()
            if t != dist[r][c] { continue }
            if r == m - 1 && c == n - 1 { return t }
            for (dr, dc) in dirs {
                let nr = r + dr, nc = c + dc
                if nr < 0 || nc < 0 || nr >= m || nc >= n { continue }
                let start = max(t, moveTime[nr][nc])
                let nt = start + 1
                if nt < dist[nr][nc] {
                    dist[nr][nc] = nt
                    h.push((nt, nr, nc))
                }
            }
        }
        return -1
    }
}
