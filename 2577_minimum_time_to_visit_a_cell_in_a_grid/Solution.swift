// LeetCode 2577 - Minimum Time to Visit a Cell In a Grid
// https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

class Solution {
    func minimumTime(_ grid: [[Int]]) -> Int {
        if grid[0][1] > 1 && grid[1][0] > 1 { return -1 }
        let m = grid.count, n = grid[0].count
        var dist = [[Int]](repeating: [Int](repeating: 1 << 30, count: n), count: m)
        var h = Heap<(Int, Int, Int)> { $0.0 < $1.0 }
        h.push((0, 0, 0))
        dist[0][0] = 0
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while !h.isEmpty {
            let cur = h.pop()
            let t = cur.0, r = cur.1, c = cur.2
            if r == m - 1 && c == n - 1 { return t }
            if t > dist[r][c] { continue }
            for d in dirs {
                let nr = r + d.0, nc = c + d.1
                if nr < 0 || nr >= m || nc < 0 || nc >= n { continue }
                var nt = t + 1
                if nt < grid[nr][nc] {
                    var wait = grid[nr][nc] - nt
                    if wait % 2 == 1 { wait += 1 }
                    nt += wait
                }
                if nt < dist[nr][nc] {
                    dist[nr][nc] = nt
                    h.push((nt, nr, nc))
                }
            }
        }
        return -1
    }

    private struct Heap<T> {
        var data = [T]()
        let less: (T, T) -> Bool
        init(_ less: @escaping (T, T) -> Bool) { self.less = less }
        var isEmpty: Bool { data.isEmpty }
        mutating func push(_ x: T) {
            data.append(x)
            var i = data.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if !less(data[i], data[p]) { break }
                data.swapAt(i, p); i = p
            }
        }
        mutating func pop() -> T {
            let res = data[0]
            let last = data.removeLast()
            if !data.isEmpty {
                data[0] = last
                var i = 0
                while true {
                    var s = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < data.count && less(data[l], data[s]) { s = l }
                    if r < data.count && less(data[r], data[s]) { s = r }
                    if s == i { break }
                    data.swapAt(i, s); i = s
                }
            }
            return res
        }
    }

}
