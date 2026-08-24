// LeetCode 2131 - Longest Palindrome by Concatenating Two Letter Words
// https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

class Solution {
    fun longestPalindrome(words: Array<String>): Int {
        var freq = HashMap()
        for (w in words) freq.merge(w, 1, Int::sum)
        var ans: Int = 0
        var center: Boolean = false
        for (kv in freq.entrySet()) {
            var w: String = kv.getKey()
            var c: Int = kv.getValue()
            var rev: String = "" + w[1] + w[0]
            if (w[0] == w[1]) {
                ans += (c / 2) * 4
                if (c % 2 != 0) center = true
            } else if (w.compareTo(rev) < 0) {
                ans += minOf(c, freq.getOrDefault(rev, 0)) * 4
            }
        }
        if (center) ans += 2
        return ans
    }
}
