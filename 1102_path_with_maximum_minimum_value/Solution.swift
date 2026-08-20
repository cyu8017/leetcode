// LeetCode 1102 - Path With Maximum Minimum Value
// https://leetcode.com/problems/path-with-maximum-minimum-value/

class Solution {
    func maximumMinimumPath(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var heap: [(Int, Int, Int)] = [(-grid[0][0], 0, 0)]
        var seen = Set<Int>([0])
        func key(_ r: Int, _ c: Int) -> Int { r * n + c }
        while !heap.isEmpty {
            heap.sort { $0.0 < $1.0 }
            let cur = heap.removeFirst()
            let val = cur.0, r = cur.1, c = cur.2
            if r == m - 1 && c == n - 1 { return -val }
            for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)] {
                let nr = r + dr, nc = c + dc
                if nr >= 0 && nr < m && nc >= 0 && nc < n {
                    let k = key(nr, nc)
                    if !seen.contains(k) {
                        seen.insert(k)
                        heap.append((max(val, -grid[nr][nc]), nr, nc))
                    }
                }
            }
        }
        return grid[0][0]
    }
}
