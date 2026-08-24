// LeetCode 2573 - Find the String with LCP
// https://leetcode.com/problems/find-the-string-with-lcp/

class Solution {
    fun findTheString(lcp: Array<IntArray>): String {
        var n = lcp.size
        var s = CharArray(n)
        var c = 'a'
        for (i in 0 until n) {
            if (s[i] != 0) continue
            if (c > 'z') return ""
            s[i] = c
            for (j in i + 1 until n) {
                if (lcp[i][j] > 0) s[j] = c
            }
            c = c + 1
        }
        for (i in n - 1 downTo 0) {
            for (j in n - 1 downTo 0) {
                var v = 0
                if (s[i] == s[j]) {
                    v = 1
                    if (i + 1 < n && j + 1 < n) v += lcp[i + 1][j + 1]
                }
                if (lcp[i][j] != v) return ""
            }
        }
        return String(s)
    }
}
