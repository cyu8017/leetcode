// LeetCode 1156 - Swap For Longest Repeated Character Substring
// https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

class Solution {
    fun maxRepOpt1(text: String): Int {
        val count = IntArray(26)
        for (ch in text) count[ch - 'a']++
        val n = text.length
        var ans = 0
        var i = 0
        while (i < n) {
            var j = i
            while (j < n && text[j] == text[i]) j++
            val length = j - i
            var k = j + 1
            while (k < n && text[k] == text[i]) k++
            val length2 = if (j < n) k - j - 1 else 0
            ans = maxOf(ans, minOf(length + length2 + 1, count[text[i] - 'a']))
            i = j
        }
        return ans
    }
}
