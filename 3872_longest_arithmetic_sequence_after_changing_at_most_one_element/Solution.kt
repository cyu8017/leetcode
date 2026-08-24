// LeetCode 3872 - Longest Arithmetic Sequence After Changing At Most One Element
// https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/

class Solution {
    fun longestArithmetic(nums: IntArray): Int {
        var n = nums.size
        var d = IntArray(n)
        for (i in 1 until n) { d[i] = nums[i] - nums[i - 1] }
        var f = IntArray(n)
        var g = IntArray(n)
        f.fill(2); g.fill(2)
        f[0] = 1
        g[n - 1] = 1
        for (i in 2 until n) {
            if (d[i] == d[i - 1]) f[i] = f[i - 1] + 1
        }
        for (i in n - 3 downTo 0) {
            if (d[i + 1] == d[i + 2]) g[i] = g[i + 1] + 1
        }
        var ans = 3
        for (i in 0 until n) {
            ans = maxOf(ans, maxOf(f[i], g[i]))
            if (i > 0) ans = maxOf(ans, f[i - 1] + 1)
            if (i + 1 < n) ans = maxOf(ans, g[i + 1] + 1)
            if (i > 0 && i < n - 1) {
                var diff = nums[i + 1] - nums[i - 1]
                if (diff % 2 == 0) {
                    diff /= 2
                    var k = 3
                    if (i > 1 && diff == d[i - 1]) k += f[i - 1] - 1
                    if (i < n - 2 && diff == d[i + 2]) k += g[i + 1] - 1
                    ans = maxOf(ans, k)
                }
            }
        }
        return ans
    }
}
