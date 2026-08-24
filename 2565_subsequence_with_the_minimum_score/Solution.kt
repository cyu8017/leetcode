// LeetCode 2565 - Subsequence With the Minimum Score
// https://leetcode.com/problems/subsequence-with-the-minimum-score/

class Solution {
    fun minimumScore(s: String, t: String): Int {
        var n = s.length
        var m = t.length
        var left = IntArray(m)
        var right = IntArray(m)
        var i: Int = 0
while (i < m) {
 left[i] = -1; right[i] = -1
i = i + 1
}
        var j = 0
        for (i in 0 until n && j < m) {
            if (s[i] == t[j]) {
                left[j] = i
                j = j + 1
            }
        }
        j = m - 1
        for (i in n - 1 downTo 0 && j >= 0) {
            if (s[i] == t[j]) {
                right[j] = i
                j = j - 1
            }
        }
        if (left[m - 1] != -1) return 0
        var ans = m
        for (i in 0 until m) {
            if (right[i] != -1) {
                if (i < ans) ans = i
                break
            }
        }
        for (i in m - 1 downTo 0) {
            if (left[i] != -1) {
                if (m - 1 - i < ans) ans = m - 1 - i
                break
            }
        }
        j = 0
        for (i in 0 until m) {
            if (left[i] == -1) break
            while (j < m && (right[j] == -1 || right[j] <= left[i])) { j = j + 1 }
            if (j < m) {
                var rem = j - i - 1
                if (rem < ans) ans = rem
            }
        }
        return ans
    }
}
