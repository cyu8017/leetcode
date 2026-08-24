// LeetCode 0840 - Magic Squares In Grid
// https://leetcode.com/problems/magic-squares-in-grid/

class Solution {
    func numMagicSquaresInside(_ grid: [[Int]]) -> Int {
        let rows = grid.count, cols = grid[0].count
        if rows < 3 || cols < 3 { return 0 }
        var ans = 0
        for i in 0..<(rows - 2) {
            for j in 0..<(cols - 2) where magic(grid, i, j) { ans += 1 }
        }
        return ans
    }

    private func magic(_ a: [[Int]], _ r: Int, _ c: Int) -> Bool {
        var vals = [Int]()
        for i in 0..<3 {
            for j in 0..<3 { vals.append(a[r + i][c + j]) }
        }
        vals.sort()
        for i in 0..<9 where vals[i] != i + 1 { return false }
        return a[r][c] + a[r][c + 1] + a[r][c + 2] == 15
            && a[r + 1][c] + a[r + 1][c + 1] + a[r + 1][c + 2] == 15
            && a[r + 2][c] + a[r + 2][c + 1] + a[r + 2][c + 2] == 15
            && a[r][c] + a[r + 1][c] + a[r + 2][c] == 15
            && a[r][c + 1] + a[r + 1][c + 1] + a[r + 2][c + 1] == 15
            && a[r][c + 2] + a[r + 1][c + 2] + a[r + 2][c + 2] == 15
            && a[r][c] + a[r + 1][c + 1] + a[r + 2][c + 2] == 15
            && a[r][c + 2] + a[r + 1][c + 1] + a[r + 2][c] == 15
    }
}
