// LeetCode 1960
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/

class Solution {
    fun maxProduct(s: String): Long {
        val n = s.length
        val radius = IntArray(n)
        var center = 0
        var right = 0
        for (i in 0 until n) {
            if (i < right) radius[i] = minOf(right - i, radius[2 * center - i])
            while (i - radius[i] - 1 >= 0 && i + radius[i] + 1 < n &&
                s[i - radius[i] - 1] == s[i + radius[i] + 1]
            ) radius[i]++
            if (i + radius[i] > right) {
                center = i
                right = i + radius[i]
            }
        }
        val end = IntArray(n) { 1 }
        val start = IntArray(n) { 1 }
        for (i in 0 until n) {
            val r = radius[i]
            end[i + r] = maxOf(end[i + r], 2 * r + 1)
            start[i - r] = maxOf(start[i - r], 2 * r + 1)
        }
        for (i in n - 2 downTo 0) end[i] = maxOf(end[i], end[i + 1] - 2)
        for (i in 1 until n) start[i] = maxOf(start[i], start[i - 1] - 2)
        val pre = IntArray(n)
        pre[0] = end[0]
        for (i in 1 until n) pre[i] = maxOf(pre[i - 1], end[i])
        val suf = IntArray(n)
        suf[n - 1] = start[n - 1]
        for (i in n - 2 downTo 0) suf[i] = maxOf(suf[i + 1], start[i])
        var ans = 0L
        for (i in 0 until n - 1) ans = maxOf(ans, pre[i].toLong() * suf[i + 1])
        return ans
    }
}
