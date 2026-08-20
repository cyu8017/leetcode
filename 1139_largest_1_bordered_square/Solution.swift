// LeetCode 1139 - Largest 1-Bordered Square
// https://leetcode.com/problems/largest-1-bordered-square/

class Solution {
    func largest1BorderedSquare(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var left = [[Int]](repeating: [Int](repeating: 0, count: n), count: m)
        var up = [[Int]](repeating: [Int](repeating: 0, count: n), count: m)
        for r in 0..<m {
            for c in 0..<n where grid[r][c] == 1 {
                left[r][c] = 1 + (c > 0 ? left[r][c - 1] : 0)
                up[r][c] = 1 + (r > 0 ? up[r - 1][c] : 0)
            }
        }
        var best = 0
        for r in 0..<m {
            for c in 0..<n where grid[r][c] == 1 {
                let limit = min(left[r][c], up[r][c])
                for size in stride(from: limit, through: 1, by: -1) {
                    if left[r - size + 1][c] >= size && up[r][c - size + 1] >= size {
                        best = max(best, size)
                        break
                    }
                }
            }
        }
        return best * best
    }
}
