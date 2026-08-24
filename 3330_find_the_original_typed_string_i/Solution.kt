// LeetCode 3330 - Find the Original Typed String I
// https://leetcode.com/problems/find-the-original-typed-string-i/

class Solution {
    fun possibleStringCount(word: String): Int {
        var ans = 1
        for (i in 1 until word.length) {
            if (word[i] == word[i - 1]) ans++
        }
        return ans
    }
}
