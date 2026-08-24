// LeetCode 1119 - Remove Vowels from a String
// https://leetcode.com/problems/remove-vowels-from-a-string/

class Solution {
    fun removeVowels(s: String): String {
        val vowels = setOf('a', 'e', 'i', 'o', 'u')
        return s.filter { it !in vowels }
    }
}
