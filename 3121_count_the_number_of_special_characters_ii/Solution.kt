// LeetCode 3121 - Count the Number of Special Characters II
// https://leetcode.com/problems/count-the-number-of-special-characters-ii/

class Solution {
    fun numberOfSpecialChars(word: String): Int {
        var first = IntArray(128), last = IntArray(128)
        for (i in 0 until word.length) {
            var c = word[i]
            if (first[c] == 0) first[c] = i + 1
            last[c] = i + 1
        }
        var ans = 0
        for (i in 0 until 26) {
            if (last['a' + i] > 0 && last['a' + i] < first['A' + i]) ans++
        }
        return ans
    }
}
