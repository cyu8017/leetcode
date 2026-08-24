// LeetCode 3884 - First Matching Character From Both Ends
// https://leetcode.com/problems/first-matching-character-from-both-ends/

class Solution {
    fun firstMatchingIndex(s: String): Int {
        var n = s.length
        for (i in 0 until n / 2 + 1) {
            if (s[i] == s[n - i - 1]) return i
        }
        return -1
    }
}
