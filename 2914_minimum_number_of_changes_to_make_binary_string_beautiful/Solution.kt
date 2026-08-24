// LeetCode 2914 - Minimum Number of Changes to Make Binary String Beautiful
// https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/


class Solution {
    fun minChanges(s: String): Int {
        var ans = 0
        var i = 0
        while (i < s.length) {
            if (s[i] != s[i + 1]) ans++
            i += 2
        }
        return ans
    }
}
