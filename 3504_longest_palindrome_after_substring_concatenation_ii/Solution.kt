// LeetCode 3504 - Longest Palindrome After Substring Concatenation II
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/

class Solution {
    fun expand(s: String, g: IntArray, l0: Int, r0: Int) {
        var l = l0
        var r = r0
        while (l >= 0 && r < s.length && s[l] == s[r]) {
            g[l] = maxOf(g[l], r - l + 1)
            l--
            r++
        }
    }

    fun calc(s: String): IntArray {
        val n = s.length
        val g = IntArray(n)
        for (i in 0 until n) {
            expand(s, g, i, i)
            expand(s, g, i, i + 1)
        }
        return g
    }

    fun longestPalindrome(s: String, t0: String): Int {
        var t = t0
        val m = s.length
        val n = t.length
        val tc = t.toCharArray()
        var i = 0
        var j = tc.size - 1
        while (i < j) {
            val tmp = tc[i]
            tc[i] = tc[j]
            tc[j] = tmp
            i++
            j--
        }
        t = String(tc)
        val g1 = calc(s)
        val g2 = calc(t)
        var ans = 0
        for (v in g1) ans = maxOf(ans, v)
        for (v in g2) ans = maxOf(ans, v)
        val f = Array(m + 1) { IntArray(n + 1) }
        for (ii in 1..m) {
            for (jj in 1..n) {
                if (s[ii - 1] == t[jj - 1]) {
                    f[ii][jj] = f[ii - 1][jj - 1] + 1
                    val a = if (ii < m) g1[ii] else 0
                    val b = if (jj < n) g2[jj] else 0
                    ans = maxOf(ans, f[ii][jj] * 2 + a)
                    ans = maxOf(ans, f[ii][jj] * 2 + b)
                }
            }
        }
        return ans
    }
}
