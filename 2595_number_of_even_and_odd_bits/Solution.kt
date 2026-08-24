// LeetCode 2595 - Number of Even and Odd Bits
// https://leetcode.com/problems/number-of-even-and-odd-bits/

class Solution {
    fun evenOddBit(n: Int): IntArray {
        var even = 0
        var odd = 0
        var x = n
        var i = 0
        while (x > 0) {
            if ((x and 1) != 0) {
                if (i % 2 == 0) even += 1 else odd += 1
            }
            i += 1
            x = x shr 1
        }
        return intArrayOf(even, odd)
    }
}
