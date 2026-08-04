// LeetCode 1100 - Find K-Length Substrings With No Repeated Characters
// https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

class Solution {
    fun numKLenSubstrNoRepeats(s: String, k: Int): Int {
        if (k > s.length) return 0
        val window = mutableMapOf<Char, Int>()
        for (i in 0 until k) {
            window[s[i]] = window.getOrDefault(s[i], 0) + 1
        }
        var ans = if (window.size == k) 1 else 0
        for (i in k until s.length) {
            window[s[i]] = window.getOrDefault(s[i], 0) + 1
            val left = s[i - k]
            val c = window.getOrDefault(left, 0) - 1
            if (c == 0) window.remove(left) else window[left] = c
            if (window.size == k) ans++
        }
        return ans
    }
}
