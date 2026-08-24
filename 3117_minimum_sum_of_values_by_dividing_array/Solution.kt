// LeetCode 3117 - Minimum Sum of Values by Dividing Array
// https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

class Solution {
    private val INF: Int = 1  shl  29
    private var nums: IntArray? = null
    private var andValues: IntArray? = null
    private var n: Int = 0
    private var m: Int = 0
    private var f: MutableMap<Long, Int>? = null

    private fun dfs(i: Int, j: Int, a: Int): Int {
        if (n - i < m - j) return INF
        if (j == m) return if (i == n) 0 else INF
        a &= nums[i]
        if (a < andValues[j]) return INF
        var key = (i  shl  36) | (j  shl  32) | (a & 0xffffffffL)
        var cached = f[key]
        if (cached != null) return cached
        var ans = dfs(i + 1, j, a)
        if (a == andValues[j]) {
            ans = minOf(ans, dfs(i + 1, j + 1, -1) + nums[i])
        }
        f[key] = ans
        return ans
    }

    fun minimumValueSum(nums: IntArray, andValues: IntArray): Int {
        this.nums = nums
        this.andValues = andValues
        this.n = nums.size
        this.m = andValues.size
        this.f = HashMap()
        var ans = dfs(0, 0, -1)
        return if (ans < INF) ans else -1
    }
}
