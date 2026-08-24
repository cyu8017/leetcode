// LeetCode 1545 - Find Kth Bit in Nth Binary String
// https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution {
    fun findKthBit(n: Int, k: Int): Char {
        var invert = false
        var length = (1 shl n) - 1
        var pos = k
        while (pos != 1) {
            val middle = length / 2 + 1
            if (pos == middle) return if (invert) '0' else '1'
            if (pos > middle) {
                pos = length - pos + 1
                invert = !invert
            }
            length /= 2
        }
        return if (invert) '1' else '0'
    }
}
