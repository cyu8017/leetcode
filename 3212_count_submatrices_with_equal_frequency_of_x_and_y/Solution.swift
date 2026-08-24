// LeetCode 3212 - Count Submatrices With Equal Frequency of X and Y
// https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

class Solution {
    func numberOfSubmatrices(_ grid: [[Character]]) -> Int {
        let m = grid.count, n = grid[0].count
        var s = Array(repeating: Array(repeating: [0, 0], count: n + 1), count: m + 1)
        var ans = 0
        for i in 1...m {
            for j in 1...n {
                s[i][j][0] = s[i - 1][j][0] + s[i][j - 1][0] - s[i - 1][j - 1][0]
                if grid[i - 1][j - 1] == "X" { s[i][j][0] += 1 }
                s[i][j][1] = s[i - 1][j][1] + s[i][j - 1][1] - s[i - 1][j - 1][1]
                if grid[i - 1][j - 1] == "Y" { s[i][j][1] += 1 }
                if s[i][j][0] > 0 && s[i][j][0] == s[i][j][1] { ans += 1 }
            }
        }
        return ans
    }
}
