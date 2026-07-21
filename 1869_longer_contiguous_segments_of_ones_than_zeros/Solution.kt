// LeetCode 1869 - Longer Contiguous Segments of Ones than Zeros
// https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

class Solution {
    fun checkZeroOnes(s: String): Boolean {
        var maxZeros = 0
        var maxOnes = 0
        var zeros = 0
        var ones = 0
        for (ch in s) {
            if (ch == '0') {
                zeros++
                ones = 0
                maxZeros = maxOf(maxZeros, zeros)
            } else {
                ones++
                zeros = 0
                maxOnes = maxOf(maxOnes, ones)
            }
        }
        return maxOnes > maxZeros
    }
}
