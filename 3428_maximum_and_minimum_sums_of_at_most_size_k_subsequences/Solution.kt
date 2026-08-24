// LeetCode 3428 - Maximum and Minimum Sums of at Most Size K Subsequences
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

class Solution {
    fun minMaxSums(nums: IntArray, k: Int): Int {
        val mod = 1_000_000_007
        nums.sort()
        var n = nums.size
        var C = Array(n + 1) { IntArray(k) }
        for (i in 0 .. n) {
            C[i][0] = 1
            for (j in 1 until k && j <= i) { C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % mod }
        }
        var ans = 0
        for (i in 0 until n) {
            var waysMax = 0
            for (j in 0 until k && j <= i) { waysMax = (waysMax + C[i][j]) % mod }
            var waysMin = 0
            var right = n - i - 1
            for (j in 0 until k && j <= right) { waysMin = (waysMin + C[right][j]) % mod }
            ans = ((ans + nums[i] * waysMax % mod + nums[i] * waysMin % mod) % mod)
        }
        return ans
    }
}
