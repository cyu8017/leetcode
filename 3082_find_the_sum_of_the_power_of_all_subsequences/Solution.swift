// LeetCode 3082 - Find the Sum of the Power of All Subsequences
// https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

class Solution {
    func sumOfPower(_ nums: [Int], _ k: Int) -> Int {
        let MOD = 1_000_000_007
        let n = nums.count
        var f = Array(repeating: Array(repeating: 0, count: k + 1), count: n + 1)
        f[0][0] = 1
        for i in 1...n {
            for j in 0...k {
                f[i][j] = (f[i - 1][j] * 2) % MOD
                if j >= nums[i - 1] {
                    f[i][j] = (f[i][j] + f[i - 1][j - nums[i - 1]]) % MOD
                }
            }
        }
        return f[n][k]
    }
}
