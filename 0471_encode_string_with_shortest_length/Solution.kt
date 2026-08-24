// LeetCode 0471 - Encode String with Shortest Length
// https://leetcode.com/problems/encode-string-with-shortest-length/

class Solution {
    fun encode(s: String): String {
        val length = s.length
        val dp = Array(length + 1) { "" }

        for (index in 1..length) {
            dp[index] = encodeWord(s.substring(0, index))
            for (split in 1 until index) {
                val candidate = dp[index - split] + encodeWord(s.substring(index - split, index))
                if (candidate.length < dp[index].length
                    || (candidate.length == dp[index].length && candidate < dp[index])
                ) {
                    dp[index] = candidate
                }
            }
        }
        return dp[length]
    }

    private fun encodeWord(word: String): String {
        val size = word.length
        var best = word
        for (unitLength in 1..size / 2) {
            if (size % unitLength != 0) {
                continue
            }
            val unit = word.substring(0, unitLength)
            if (unit.repeat(size / unitLength) == word) {
                val encoded = "${size / unitLength}[$unit]"
                if (encoded.length < best.length
                    || (encoded.length == best.length && encoded < best)
                ) {
                    best = encoded
                }
            }
        }
        return best
    }
}
