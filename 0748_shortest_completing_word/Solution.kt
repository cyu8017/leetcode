// LeetCode 0748 - Shortest Completing Word
// https://leetcode.com/problems/shortest-completing-word/

class Solution {
    fun shortestCompletingWord(licensePlate: String, words: Array<String>): String {
        val need = IntArray(26)
        for (ch in licensePlate) {
            if (ch.isLetter()) need[ch.lowercaseChar() - 'a']++
        }
        var best = ""
        for (word in words) {
            val counts = IntArray(26)
            for (ch in word) counts[ch - 'a']++
            var ok = true
            for (i in 0 until 26) {
                if (counts[i] < need[i]) {
                    ok = false
                    break
                }
            }
            if (ok && (best.isEmpty() || word.length < best.length)) best = word
        }
        return best
    }
}
