// LeetCode 3227 - Vowels Game in a String
// https://leetcode.com/problems/vowels-game-in-a-string/

class Solution {
    fun doesAliceWin(s: String): Boolean {
        for (i in 0 until s.length) {
            var c = s[i]
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') return true
        }
        return false
    }
}
