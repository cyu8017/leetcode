// LeetCode 1631 - Path With Minimum Effort
// https://leetcode.com/problems/path-with-minimum-effort/

private struct EffortHeap {
    private var data = [(Int, Int, Int)]()
    var isEmpty: Bool { data.isEmpty }
    mutating func push(_ item: (Int, Int, Int)) {
        data.append(item)
        var i = data.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if data[p].0 <= data[i].0 { break }
            data.swapAt(p, i)
            i = p
        }
    }
    mutating func pop() -> (Int, Int, Int) {
        let result = data[0]
        let last = data.removeLast()
        if !data.isEmpty {
            data[0] = last
            var i = 0
            while true {
                var best = i
                let l = 2 * i + 1, r = l + 1
                if l < data.count && data[l].0 < data[best].0 { best = l }
                if r < data.count && data[r].0 < data[best].0 { best = r }
                if best == i { break }
                data.swapAt(i, best)
                i = best
            }
        }
        return result
    }
}

class Solution {
    func minimumEffortPath(_ heights: [[Int]]) -> Int {
        let m = heights.count, n = heights[0].count
        var dist = [[Int]](repeating: [Int](repeating: Int.max, count: n), count: m)
        dist[0][0] = 0
        var heap = EffortHeap()
        heap.push((0, 0, 0))
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while !heap.isEmpty {
            let (effort, i, j) = heap.pop()
            if i == m - 1 && j == n - 1 { return effort }
            if effort != dist[i][j] { continue }
            for (di, dj) in dirs {
                let x = i + di, y = j + dj
                if x >= 0 && x < m && y >= 0 && y < n {
                    let nd = max(effort, abs(heights[i][j] - heights[x][y]))
                    if nd < dist[x][y] {
                        dist[x][y] = nd
                        heap.push((nd, x, y))
                    }
                }
            }
        }
        return 0
    }
}
