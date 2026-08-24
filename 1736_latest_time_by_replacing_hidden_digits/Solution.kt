// LeetCode 1736 - Latest Time by Replacing Hidden Digits
// https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/

class Solution {
    fun maximumTime(time: String): String {
        val chars = time.toCharArray()
        if (chars[0] == '?') {
            chars[0] = if (chars[1] in "0123?") '2' else '1'
        }
        if (chars[1] == '?') {
            chars[1] = if (chars[0] == '2') '3' else '9'
        }
        if (chars[3] == '?') {
            chars[3] = '5'
        }
        if (chars[4] == '?') {
            chars[4] = '9'
        }
        return String(chars)
    }
}
