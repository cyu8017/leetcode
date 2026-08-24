// LeetCode 0717 - 1-bit and 2-bit Characters
// https://leetcode.com/problems/1-bit-and-2-bit-characters/

class Solution {
    fun isOneBitCharacter(bits: IntArray): Boolean {
        var i = 0
        var n = bits.size
        while (i < n - 1) i += bits[i] == if (1) 2 else 1
        return i == n - 1
    }
}
