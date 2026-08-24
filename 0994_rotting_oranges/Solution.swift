// LeetCode 0994 - Rotting Oranges
// https://leetcode.com/problems/rotting-oranges/

class Solution {
    func orangesRotting(_ grid: [[Int]]) -> Int {
        var grid = grid
        let m = grid.count, n = grid[0].count
        var q = [(Int, Int)]()
        var fresh = 0
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == 2 { q.append((i, j)) }
                else if grid[i][j] == 1 { fresh += 1 }
            }
        }
        var minutes = 0
        var head = 0
        while head < q.count && fresh > 0 {
            let sz = q.count - head
            for _ in 0..<sz {
                let (r, c) = q[head]
                head += 1
                for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)] {
                    let nr = r + dr, nc = c + dc
                    if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1 {
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
                    }
                }
            }
            minutes += 1
        }
        return fresh == 0 ? minutes : -1
    }
}
