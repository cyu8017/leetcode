// LeetCode 2906 - Construct Product Matrix
// https://leetcode.com/problems/construct-product-matrix/

class Solution {
    func constructProductMatrix(_ grid: [[Int]]) -> [[Int]] {
        let mod = 12345
        let m = grid.count, n = grid[0].count
        var ans = Array(repeating: Array(repeating: 0, count: n), count: m)
        var pref = 1
        for i in 0..<m {
            for j in 0..<n {
                ans[i][j] = pref
                pref = pref * (grid[i][j] % mod) % mod
            }
        }
        var suf = 1
        for i in stride(from: m - 1, through: 0, by: -1) {
            for j in stride(from: n - 1, through: 0, by: -1) {
                ans[i][j] = ans[i][j] * suf % mod
                suf = suf * (grid[i][j] % mod) % mod
            }
        }
        return ans
    }
}
