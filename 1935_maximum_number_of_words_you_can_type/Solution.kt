// LeetCode 1935
// https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution {
    fun canBeTypedWords(text: String, brokenLetters: String): Int {
        val broken = brokenLetters.toSet()
        return text.split(" ").count { w -> w.none { it in broken } }
    }
}
