// LeetCode 1009 - Complement of Base 10 Integer
// https://leetcode.com/problems/complement-of-base-10-integer/

class Solution {
    fun bitwiseComplement(n: Int): Int {
        if (n == 0) return 1
        var mask = 1
        while (mask <= n) mask = mask shl 1
        return n xor (mask - 1)
    }
}
