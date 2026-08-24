// LeetCode 3125 - Maximum Number That Makes Result of Bitwise AND Zero
// https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/

class Solution {
    fun maxNumber(n: Long): Long {
        var len = 64 - Long.numberOfLeadingZeros(n)
        return (1L  shl  (len - 1)) - 1
    }
}
