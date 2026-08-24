// LeetCode 0693 - Binary Number with Alternating Bits
// https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution {
    fun hasAlternatingBits(n: Int): Boolean {
        var x = n ^ (n  ushr  1)
        return (x & (x + 1)) == 0
    }
}
