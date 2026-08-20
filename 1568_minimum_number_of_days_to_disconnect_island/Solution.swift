// LeetCode 1568 - Minimum Number of Days to Disconnect Island
// https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

class Solution {
    func minDays(_ grid: [[Int]]) -> Int {
        var grid = grid
        let m = grid.count, n = grid[0].count
        func islands() -> Int {
            var seen = Set<Int>()
            var count = 0
            func key(_ r: Int, _ c: Int) -> Int { r * n + c }
            for r in 0..<m {
                for c in 0..<n {
                    if grid[r][c] == 1 && !seen.contains(key(r, c)) {
                        count += 1
                        var stack = [(r, c)]
                        seen.insert(key(r, c))
                        while let (x, y) = stack.popLast() {
                            for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)] {
                                let nx = x + dx, ny = y + dy
                                if nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1 && !seen.contains(key(nx, ny)) {
                                    seen.insert(key(nx, ny))
                                    stack.append((nx, ny))
                                }
                            }
                        }
                    }
                }
            }
            return count
        }
        if islands() != 1 { return 0 }
        for r in 0..<m {
            for c in 0..<n where grid[r][c] == 1 {
                grid[r][c] = 0
                if islands() != 1 {
                    grid[r][c] = 1
                    return 1
                }
                grid[r][c] = 1
            }
        }
        return 2
    }
}
