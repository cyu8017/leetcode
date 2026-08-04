// LeetCode 1297 - Maximum Number of Occurrences of a Substring
// https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

class Solution {
    fun maxFreq(s: String, maxLetters: Int, minSize: Int, maxSize: Int): Int {
        val counts = mutableMapOf<String, Int>()
        for (i in 0..s.length - minSize) {
            val sub = s.substring(i, i + minSize)
            if (sub.toSet().size <= maxLetters) {
                counts[sub] = counts.getOrDefault(sub, 0) + 1
            }
        }
        return counts.values.maxOrNull() ?: 0
    }
}
