// LeetCode 3094 - Guess the Number Using Bitwise Questions II
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/

/**
 * Definition of commonBits API.
 * int commonBits(int num)
 */

class Solution : Guess() {
    fun findNumber(): Int {
        var n = 0
        for (i in 0 until 32) {
            var count1 = commonBits(1  shl  i)
            var count2 = commonBits(1  shl  i)
            if (count1 > count2) n |= 1  shl  i
        }
        return n
    }
}
