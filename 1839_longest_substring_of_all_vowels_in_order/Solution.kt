// LeetCode 1839 - Longest Substring Of All Vowels in Order
// https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

class Solution {
    fun longestBeautifulSubstring(word: String): Int {
        val vowels = "aeiou"
        var best = 0
        for (start in word.indices) {
            if (word[start] != 'a') continue
            val counts = IntArray(5)
            for (end in start until word.length) {
                val current = word[end]
                if (end > start && current < word[end - 1]) break
                val idx = vowels.indexOf(current)
                if (idx < 0) break
                counts[idx]++
                if (idx > 0 && counts[idx - 1] == 0) break
                if (counts.all { it > 0 }) best = maxOf(best, end - start + 1)
            }
        }
        return best
    }
}
