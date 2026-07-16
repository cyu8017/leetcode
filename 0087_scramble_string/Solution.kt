// LeetCode 0087 - Scramble String
// https://leetcode.com/problems/scramble-string/

class Solution {
    private val memo = HashMap<String, Boolean>()

    fun isScramble(s1: String, s2: String): Boolean {
        val key = "$s1#$s2"
        memo[key]?.let { return it }
        if (s1 == s2) {
            memo[key] = true
            return true
        }
        if (s1.toCharArray().sorted() != s2.toCharArray().sorted()) {
            memo[key] = false
            return false
        }

        val n = s1.length
        for (i in 1 until n) {
            if (isScramble(s1.substring(0, i), s2.substring(0, i))
                && isScramble(s1.substring(i), s2.substring(i))
            ) {
                memo[key] = true
                return true
            }
            if (isScramble(s1.substring(0, i), s2.substring(n - i))
                && isScramble(s1.substring(i), s2.substring(0, n - i))
            ) {
                memo[key] = true
                return true
            }
        }
        memo[key] = false
        return false
    }
}
