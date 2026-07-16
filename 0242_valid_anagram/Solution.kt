// LeetCode 0242 - Valid Anagram
// https://leetcode.com/problems/valid-anagram/

class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        if (s.length != t.length) {
            return false
        }
        val counts = IntArray(26)
        for (index in s.indices) {
            counts[s[index] - 'a']++
            counts[t[index] - 'a']--
        }
        return counts.all { it == 0 }
    }
}
