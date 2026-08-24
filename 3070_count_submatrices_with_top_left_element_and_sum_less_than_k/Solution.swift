// LeetCode 3070 - Count Submatrices with Top-Left Element and Sum Less Than k
// https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

class Solution {
    func countSubmatrices(_ grid: [[Int]], _ k: Int) -> Int {
        let n = grid.count, m = grid[0].count
        var ans = 0
        var s = Array(repeating: Array(repeating: 0, count: m + 1), count: n + 1)
        for i in 0..<n {
            for j in 0..<m {
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + grid[i][j]
                if s[i + 1][j + 1] <= k { ans += 1 }
            }
        }
        return ans
    }
}
