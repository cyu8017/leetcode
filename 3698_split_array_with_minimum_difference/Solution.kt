// LeetCode 3698 - Split Array With Minimum Difference
// https://leetcode.com/problems/split-array-with-minimum-difference/

class Solution {
    fun splitArray(nums: IntArray): Long {
        val n = nums.size
        val s = LongArray(n)
        val f = BooleanArray(n) { true }
        val g = BooleanArray(n) { true }
        s[0] = nums[0].toLong()
        for (i in 1 until n) {
            s[i] = s[i - 1] + nums[i]
            f[i] = f[i - 1]
            if (nums[i] <= nums[i - 1]) f[i] = false
        }
        for (i in n - 2 downTo 0) {
            g[i] = g[i + 1]
            if (nums[i] <= nums[i + 1]) g[i] = false
        }
        val inf = Long.MAX_VALUE / 4
        var ans = inf
        for (i in 0 until n - 1) {
            if (f[i] && g[i + 1]) {
                val s1 = s[i]
                val s2 = s[n - 1] - s[i]
                ans = minOf(ans, kotlin.math.abs(s1 - s2))
            }
        }
        return if (ans < inf) ans else -1
    }
}
