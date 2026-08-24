// LeetCode 0299 - Bulls and Cows
// https://leetcode.com/problems/bulls-and-cows/

class Solution {
    fun getHint(secret: String, guess: String): String {
        var bulls = 0
        val secretCounts = mutableMapOf<Char, Int>()
        val guessCounts = mutableMapOf<Char, Int>()
        for (index in secret.indices) {
            val secretDigit = secret[index]
            val guessDigit = guess[index]
            if (secretDigit == guessDigit) {
                bulls++
            } else {
                secretCounts[secretDigit] = secretCounts.getOrDefault(secretDigit, 0) + 1
                guessCounts[guessDigit] = guessCounts.getOrDefault(guessDigit, 0) + 1
            }
        }
        val cows = guessCounts.entries.sumOf { (digit, count) ->
            minOf(count, secretCounts.getOrDefault(digit, 0))
        }
        return "${bulls}A${cows}B"
    }
}
