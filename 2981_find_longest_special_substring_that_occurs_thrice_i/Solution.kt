// LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

class Solution {
    fun maximumLength(s: String): Int {
        var n = s.length
        var ans = -1
        for (i in 0 until n) {
            for (j in i until n) {
                if (s[j] != s[i]) break
                var len = j - i + 1
                var cnt = 0
                var k = 0
                while (k + len <= n) {
                    var ok = true
                    for (t in 0 until len) {
                        if (s[k + t] != s[i + t]) { ok = false; break; }
                    }
                    if (ok) cnt++
                    k++
                }
                if (cnt >= 3 && len > ans) ans = len
            }
        }
        return ans
    }
}
