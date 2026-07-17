// LeetCode 1704 - Determine if String Halves Are Alike
// https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution {
    fun halvesAreAlike(s: String): Boolean {
        val vowels = "aeiouAEIOU"
        val mid = s.length / 2
        var balance = 0
        for (i in s.indices) {
            if (s[i] in vowels) {
                balance += if (i < mid) 1 else -1
            }
        }
        return balance == 0
    }
}
