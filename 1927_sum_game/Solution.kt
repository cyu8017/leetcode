// LeetCode 1927
// https://leetcode.com/problems/sum-game/

class Solution {
    fun sumGame(num: String): Boolean {
        val half = num.length / 2
        fun score(s: String): Int {
            var q = 0
            var dig = 0
            for (c in s) {
                if (c == '?') q++ else dig += c - '0'
            }
            return dig * 2 + q * 9
        }
        return score(num.substring(0, half)) != score(num.substring(half))
    }
}
