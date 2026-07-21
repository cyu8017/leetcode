// LeetCode 1810 - Minimum Path Cost in a Hidden Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/

class Solution {
    // Test harness passes the revealed grid plus start/target coordinates.
    func findShortestPath(_ grid: [[Int]], _ r1: Int, _ c1: Int, _ r2: Int, _ c2: Int) -> Int {
        if r1 == r2 && c1 == c2 { return 0 }
        let m = grid.count
        let n = grid[0].count
        let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        var dist = Array(repeating: Array(repeating: Int.max, count: n), count: m)
        var heap: [(Int, Int, Int)] = [(0, r1, c1)]
        dist[r1][c1] = 0

        func push(_ item: (Int, Int, Int)) {
            heap.append(item)
            var i = heap.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if heap[p].0 <= heap[i].0 { break }
                heap.swapAt(p, i)
                i = p
            }
        }
        func pop() -> (Int, Int, Int) {
            let top = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                var i = 0
                while true {
                    var smallest = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < heap.count && heap[l].0 < heap[smallest].0 { smallest = l }
                    if r < heap.count && heap[r].0 < heap[smallest].0 { smallest = r }
                    if smallest == i { break }
                    heap.swapAt(i, smallest)
                    i = smallest
                }
            }
            return top
        }

        while !heap.isEmpty {
            let (d, r, c) = pop()
            if r == r2 && c == c2 { return d }
            if d > dist[r][c] { continue }
            for (dr, dc) in dirs {
                let nr = r + dr
                let nc = c + dc
                if nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 0 { continue }
                let nd = d + grid[nr][nc]
                if nd < dist[nr][nc] {
                    dist[nr][nc] = nd
                    push((nd, nr, nc))
                }
            }
        }
        return -1
    }
}
