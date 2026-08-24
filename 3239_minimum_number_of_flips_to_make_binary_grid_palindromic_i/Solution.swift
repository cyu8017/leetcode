// LeetCode 3239 - Minimum Number of Flips to Make Binary Grid Palindromic I
// https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/

class Solution {
    func minFlips(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var cnt1 = 0, cnt2 = 0
        for row in grid {
            for j in 0..<(n / 2) where row[j] != row[n - j - 1] { cnt1 += 1 }
        }
        for j in 0..<n {
            for i in 0..<(m / 2) where grid[i][j] != grid[m - i - 1][j] { cnt2 += 1 }
        }
        return min(cnt1, cnt2)
    }
}
