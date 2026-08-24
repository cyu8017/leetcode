// LeetCode 3120 - Count the Number of Special Characters I
// https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution {
    fun numberOfSpecialChars(word: String): Int {
        var s = BooleanArray(128)
        for (i in 0 until word.length) { s[word[i]] = true }
        var ans = 0
        for (i in 0 until 26) {
            if (s['a' + i] && s['A' + i]) ans++
        }
        return ans
    }
}
