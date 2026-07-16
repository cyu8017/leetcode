// LeetCode 0140 - Word Break II
// https://leetcode.com/problems/word-break-ii/

class Solution {
    fun wordBreak(s: String, wordDict: List<String>): List<String> {
        val words = wordDict.toHashSet()
        val memo = HashMap<Int, List<String>>()
        fun sentences(start: Int): List<String> {
            memo[start]?.let { return it }
            val result = mutableListOf<String>()
            if (start == s.length) result.add("")
            else for (end in start + 1..s.length) {
                val word = s.substring(start, end)
                if (word !in words) continue
                for (tail in sentences(end)) result.add(if (tail.isEmpty()) word else "$word $tail")
            }
            memo[start] = result
            return result
        }
        return sentences(0)
    }
}
