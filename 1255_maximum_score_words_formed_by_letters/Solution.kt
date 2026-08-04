// LeetCode 1255 - Maximum Score Words Formed by Letters
// https://leetcode.com/problems/maximum-score-words-formed-by-letters/

class Solution {
    fun maxScoreWords(words: Array<String>, letters: CharArray, score: IntArray): Int {
        val available = IntArray(26)
        for (ch in letters) available[ch - 'a']++
        val counts = Array(words.size) { IntArray(26) }
        val values = IntArray(words.size)
        for (i in words.indices) {
            for (ch in words[i]) {
                counts[i][ch - 'a']++
                values[i] += score[ch - 'a']
            }
        }
        fun canUse(need: IntArray): Boolean {
            for (j in 0 until 26) if (need[j] > available[j]) return false
            return true
        }
        fun apply(need: IntArray, sign: Int) {
            for (j in 0 until 26) available[j] += sign * need[j]
        }
        fun dfs(i: Int): Int {
            if (i == words.size) return 0
            var best = dfs(i + 1)
            if (canUse(counts[i])) {
                apply(counts[i], -1)
                best = maxOf(best, values[i] + dfs(i + 1))
                apply(counts[i], 1)
            }
            return best
        }
        return dfs(0)
    }
}
