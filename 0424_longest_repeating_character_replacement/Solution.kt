// LeetCode 0424 - Longest Repeating Character Replacement
// https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution {
    fun characterReplacement(s: String, k: Int): Int {
        val counts = IntArray(26)
        var left = 0
        var best = 0
        var maxCount = 0

        for (right in s.indices) {
            val index = s[right].code - 'A'.code
            counts[index]++
            maxCount = maxOf(maxCount, counts[index])
            while ((right - left + 1) - maxCount > k) {
                val leftIndex = s[left].code - 'A'.code
                counts[leftIndex]--
                left++
            }
            best = maxOf(best, right - left + 1)
        }

        return best
    }
}
