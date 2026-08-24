// LeetCode 0273 - Integer to English Words
// https://leetcode.com/problems/integer-to-english-words/

class Solution {
    private val ones = arrayOf(
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
        "Seventeen", "Eighteen", "Nineteen"
    )
    private val tens = arrayOf(
        "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
    )
    private val thousands = arrayOf("", "Thousand", "Million", "Billion")

    fun numberToWords(num: Int): String {
        if (num == 0) {
            return "Zero"
        }

        val parts = mutableListOf<String>()
        var value = num
        var chunkIndex = 0
        while (value > 0) {
            val chunk = value % 1000
            if (chunk != 0) {
                var chunkWords = convertChunk(chunk)
                if (thousands[chunkIndex].isNotEmpty()) {
                    chunkWords += " ${thousands[chunkIndex]}"
                }
                parts.add(chunkWords)
            }
            value /= 1000
            chunkIndex++
        }
        return parts.asReversed().joinToString(" ")
    }

    private fun convertChunk(value: Int): String {
        if (value == 0) {
            return ""
        }
        if (value < 20) {
            return ones[value]
        }
        if (value < 100) {
            val tensPart = tens[value / 10]
            val onesPart = ones[value % 10]
            return if (onesPart.isEmpty()) tensPart else "$tensPart $onesPart"
        }
        val hundreds = ones[value / 100]
        val remainder = convertChunk(value % 100)
        return if (remainder.isEmpty()) "$hundreds Hundred" else "$hundreds Hundred $remainder"
    }
}
