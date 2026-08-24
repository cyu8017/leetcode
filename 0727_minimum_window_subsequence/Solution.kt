// LeetCode 0727 - Minimum Window Subsequence
// https://leetcode.com/problems/minimum-window-subsequence/

class Solution {
    fun minWindow(s1: String, s2: String): String {
        var m = s1.length
        var n = s2.length
        var best = ""
        var i = 0
        while (i < m) {
            var j = 0
            var k = i
            while (k < m && j < n) {
                if (s1[k] == s2[j]) j++
                k++
            }
            if (j < n) break
            var end = k - 1
            j = n - 1
            k = end
            while (j >= 0) {
                if (s1[k] == s2[j]) j--
                k--
            }
            var start = k + 1
            if (best.isEmpty() || end - start + 1 < best.length) best = s1.substring(start, end + 1)
            i = start + 1
        }
        return best
    }
}
