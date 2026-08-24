// LeetCode 0438 - Find All Anagrams in a String
// https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution {
    fun findAnagrams(s: String, p: String): List<Int> {
        if (p.length > s.length) {
            return emptyList()
        }

        val need = IntArray(26)
        val window = IntArray(26)
        for (char in p) {
            need[char - 'a']++
        }

        val result = mutableListOf<Int>()
        var left = 0
        for (right in s.indices) {
            window[s[right] - 'a']++
            if (right - left + 1 > p.length) {
                window[s[left] - 'a']--
                left++
            }
            if (window.contentEquals(need)) {
                result.add(left)
            }
        }
        return result
    }
}
