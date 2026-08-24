// LeetCode 3298 - Count Substrings That Can Be Rearranged to Contain a String II
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/

class Solution {
    fun validSubstringCount(word1: String, word2: String): Long {
        var need = IntArray(26)
        var required = 0
        for (c in word2.toCharArray()) {
            if (need[c - 'a'] == 0) required++
            need[c - 'a'] = need[c - 'a'] + 1
        }
        var have = IntArray(26)
        var formed = 0
        var ans = 0
        var l = 0
        for (r in 0 until word1.length) {
            var c = word1[r] - 'a'
            have[c] = have[c] + 1
            if (have[c] == need[c] && need[c] > 0) formed++
            while (formed == required && l <= r) {
                ans += word1.length - r
                var c2 = word1[l] - 'a'
                if (have[c2] == need[c2] && need[c2] > 0) formed--
                have[c2] = have[c2] - 1
                l++
            }
        }
        return ans
    }
}
