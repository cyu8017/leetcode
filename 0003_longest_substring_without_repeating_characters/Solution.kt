// LeetCode 0003 - Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        val last = HashMap<Char, Int>()
        var best = 0
        var start = 0

        for (i in s.indices) {
            val ch = s[i]
            if (last.containsKey(ch) && last[ch]!! >= start) {
                start = last[ch]!! + 1
            }
            last[ch] = i
            best = maxOf(best, i - start + 1)
        }

        return best
    }
}
