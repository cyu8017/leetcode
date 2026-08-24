// LeetCode 2351 - First Letter to Appear Twice
// https://leetcode.com/problems/first-letter-to-appear-twice/

class Solution {
    fun repeatedCharacter(s: String): Char {
        val seen = BooleanArray(26)
        for (c in s) {
            val i = c - 'a'
            if (seen[i]) return c
            seen[i] = true
        }
        return 0.toChar()
    }
}
