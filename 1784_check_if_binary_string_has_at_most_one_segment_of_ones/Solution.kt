// LeetCode 1784 - Check if Binary String Has at Most One Segment of Ones
// https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

class Solution {
    fun checkOnesSegment(s: String): Boolean {
        val trimmed = s.trim('0')
        return !trimmed.contains("01")
    }
}
