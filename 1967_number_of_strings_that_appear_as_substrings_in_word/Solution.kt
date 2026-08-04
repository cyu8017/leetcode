// LeetCode 1967
// https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

class Solution {
    fun numOfStrings(patterns: Array<String>, word: String): Int =
        patterns.count { it in word }
}
