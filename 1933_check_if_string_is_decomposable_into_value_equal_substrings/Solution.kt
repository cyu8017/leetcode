// LeetCode 1933
// https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/

class Solution {
    fun isDecomposable(s: String): Boolean {
        var i = 0
        var twos = 0
        val n = s.length
        while (i < n) {
            var j = i
            while (j < n && s[j] == s[i]) j++
            val length = j - i
            if (length % 3 == 1) return false
            if (length % 3 == 2) {
                twos++
                if (twos > 1) return false
            }
            i = j
        }
        return twos == 1
    }
}
