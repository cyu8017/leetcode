// LeetCode 0058 - Length of Last Word
// https://leetcode.com/problems/length-of-last-word/

class Solution {
    fun lengthOfLastWord(s: String): Int {
        var length = 0
        var i = s.lastIndex

        while (i >= 0 && s[i] == ' ') {
            i--
        }

        while (i >= 0 && s[i] != ' ') {
            length++
            i--
        }

        return length
    }
}
