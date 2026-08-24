// LeetCode 3082 - Find the Sum of the Power of All Subsequences
// https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

class Solution {
    fun sumOfPower(nums: IntArray, k: Int): Int {
        val MOD = 1_000_000_007
        var n = nums.size
        var f = Array(n + 1) { IntArray(k + 1) }
        f[0][0] = 1
        for (i in 1 until = n) {
            for (j in 0 until = k) {
                f[i][j] = ((f[i - 1][j] * 2L) % MOD)
                if (j >= nums[i - 1])
                    f[i][j] = (f[i][j] + f[i - 1][j - nums[i - 1]]) % MOD
            }
        }
        return f[n][k]
    }
}
