// LeetCode 3713 - Longest Balanced Substring I
// https://leetcode.com/problems/longest-balanced-substring-i/

class Solution {
    fun longestBalanced(s: String): Int {
        var n = s.length
        var ans = 0
        for (i in 0 until n) {
            var cnt = IntArray(26)
            var mx = 0
            var v = 0
            for (j in i until n) {
                var c = s[j] - 'a'
                cnt[c]++
                if (cnt[c] == 1) v++
                mx = maxOf(mx, cnt[c])
                if (mx * v == j - i + 1) ans = maxOf(ans, j - i + 1)
            }
        }
        return ans
    }
}
