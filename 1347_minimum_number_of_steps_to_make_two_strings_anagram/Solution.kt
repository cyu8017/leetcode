// LeetCode 1347 - Minimum Number of Steps to Make Two Strings Anagram
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

class Solution {
    fun minSteps(s: String, t: String): Int {
        val count = IntArray(26)
        for (c in s) count[c - 'a']++
        for (c in t) count[c - 'a']--
        var steps = 0
        for (c in count) if (c > 0) steps += c
        return steps
    }
}
