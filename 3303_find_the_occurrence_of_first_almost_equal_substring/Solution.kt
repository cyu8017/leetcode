// LeetCode 3303 - Find the Occurrence of First Almost Equal Substring
// https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

class Solution {
    fun minStartingIndex(s: String, pattern: String): Int {
        var n = s.length
        var m = pattern.length
        var i = 0
        while (i + m <= n) {
            var diff = 0
            for (j in 0 until m) {
                if (s[i + j] != pattern[j]) {
                    diff++
                    if (diff > 1) break
                }
            }
            if (diff <= 1) return i
            i++
        }
        return -1
    }
}
