// LeetCode 1160 - Find Words That Can Be Formed by Characters
// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution {
    fun countCharacters(words: Array<String>, chars: String): Int {
        val avail = IntArray(26)
        for (c in chars) avail[c - 'a']++
        var ans = 0
        for (word in words) {
            val need = IntArray(26)
            var ok = true
            for (c in word) {
                if (++need[c - 'a'] > avail[c - 'a']) {
                    ok = false
                    break
                }
            }
            if (ok) ans += word.length
        }
        return ans
    }
}
