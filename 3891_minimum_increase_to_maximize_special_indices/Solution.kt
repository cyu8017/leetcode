// LeetCode 3891 - Minimum Increase To Maximize Special Indices
// https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

class Solution {
    private var nums: IntArray? = null
    private var f: Array<LongArray>? = null
    private var n: Int = 0

    fun minIncrease(nums: IntArray): Long {
        this.nums = nums
        n = nums.size
        f = Array(n) { LongArray(2) }
        for (i in 0 until n) { f[i][0] = f[i][1] = -1 }
        return dfs(1, (n & 1) ^ 1)
    }

    private fun dfs(i: Int, j: Int): Long {
        if (i >= n - 1) return 0
        if (f[i][j] != -1) return f[i][j]
        var cost = maxOf(0, maxOf(nums[i - 1], nums[i + 1]) + 1 - nums[i])
        var ans = cost + dfs(i + 2, j)
        if (j > 0) ans = minOf(ans, dfs(i + 1, 0))
        return f[i][j] = ans
    }
}
