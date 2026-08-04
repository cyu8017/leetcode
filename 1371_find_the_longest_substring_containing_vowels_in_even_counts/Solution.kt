// LeetCode 1371 - Find the Longest Substring Containing Vowels in Even Counts
// https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution {
    fun findTheLongestSubstring(s: String): Int {
        val first = mutableMapOf(0 to -1)
        var mask = 0
        var ans = 0
        val vowels = "aeiou"
        for (i in s.indices) {
            val idx = vowels.indexOf(s[i])
            if (idx >= 0) mask = mask xor (1 shl idx)
            if (mask in first) ans = maxOf(ans, i - first[mask]!!)
            else first[mask] = i
        }
        return ans
    }
}
