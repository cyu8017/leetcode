// LeetCode 0520 - Detect Capital
// https://leetcode.com/problems/detect-capital/

class Solution {
    fun detectCapitalUse(word: String): Boolean {
        return word == word.uppercase() ||
            word == word.lowercase() ||
            word == word.replaceFirstChar { if (it.isLowerCase()) it.titlecase() else it.toString() } +
            word.drop(1).lowercase()
    }
}
