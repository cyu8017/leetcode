// LeetCode 3240 - Minimum Number of Flips to Make Binary Grid Palindromic II
// https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/

class Solution {
    func minFlips(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var ans = 0
        for i in 0..<(m / 2) {
            for j in 0..<(n / 2) {
                let x = m - i - 1, y = n - j - 1
                let cnt1 = grid[i][j] + grid[x][j] + grid[i][y] + grid[x][y]
                ans += min(cnt1, 4 - cnt1)
            }
        }
        if m % 2 == 1 && n % 2 == 1 { ans += grid[m / 2][n / 2] }
        var diff = 0, ones = 0
        if m % 2 == 1 {
            for j in 0..<(n / 2) {
                if grid[m / 2][j] == grid[m / 2][n - j - 1] { ones += grid[m / 2][j] * 2 }
                else { diff += 1 }
            }
        }
        if n % 2 == 1 {
            for i in 0..<(m / 2) {
                if grid[i][n / 2] == grid[m - i - 1][n / 2] { ones += grid[i][n / 2] * 2 }
                else { diff += 1 }
            }
        }
        if ones % 4 == 0 || diff > 0 { ans += diff }
        else { ans += 2 }
        return ans
    }
}
