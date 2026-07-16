// LeetCode 0423 - Reconstruct Original Digits from English
// https://leetcode.com/problems/reconstruct-original-digits-from-english/

class Solution {
    fun originalDigits(s: String): String {
        val counts = IntArray(26)
        for (char in s) {
            counts[char.code - 'a'.code]++
        }

        val digitCounts = IntArray(10)
        digitCounts[0] = counts['z'.code - 'a'.code]
        digitCounts[2] = counts['w'.code - 'a'.code]
        digitCounts[4] = counts['u'.code - 'a'.code]
        digitCounts[6] = counts['x'.code - 'a'.code]
        digitCounts[8] = counts['g'.code - 'a'.code]
        digitCounts[1] = counts['o'.code - 'a'.code] - digitCounts[0] - digitCounts[2] - digitCounts[4]
        digitCounts[3] = counts['h'.code - 'a'.code] - digitCounts[8]
        digitCounts[5] = counts['f'.code - 'a'.code] - digitCounts[4]
        digitCounts[7] = counts['s'.code - 'a'.code] - digitCounts[6]
        digitCounts[9] = counts['i'.code - 'a'.code] - digitCounts[5] - digitCounts[6] - digitCounts[8]

        return buildString {
            for (digit in 0..9) {
                repeat(digitCounts[digit]) {
                    append(digit)
                }
            }
        }
    }
}
