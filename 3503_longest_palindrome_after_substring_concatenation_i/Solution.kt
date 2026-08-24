// LeetCode 3503 - Longest Palindrome After Substring Concatenation I
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/

class Solution {
    private fun expand(s: String, g: IntArray, l0: Int, r0: Int) {
        var l = l0
        var r = r0
        while (l >= 0 && r < s.length && s[l] == s[r]) {
            g[l] = maxOf(g[l], r - l + 1)
            l--
            r++
        }
    }

    private fun calc(s: String): IntArray {
        val n = s.length
        val g = IntArray(n)
        for (i in 0 until n) {
            expand(s, g, i, i)
            expand(s, g, i, i + 1)
        }
        return g
    }

    fun longestPalindrome(s: String, t: String): Int {
        val m = s.length
        val n = t.length
        val tr = StringBuilder(t).reverse().toString()
        val g1 = calc(s)
        val g2 = calc(tr)
        var ans = 0
        for (v in g1) ans = maxOf(ans, v)
        for (v in g2) ans = maxOf(ans, v)
        val f = Array(m + 1) { IntArray(n + 1) }
        for (i in 1..m) {
            for (j in 1..n) {
                if (s[i - 1] == tr[j - 1]) {
                    f[i][j] = f[i - 1][j - 1] + 1
                    val a = if (i < m) g1[i] else 0
                    val b = if (j < n) g2[j] else 0
                    ans = maxOf(ans, f[i][j] * 2 + a)
                    ans = maxOf(ans, f[i][j] * 2 + b)
                }
            }
        }
        return ans
    }
}
