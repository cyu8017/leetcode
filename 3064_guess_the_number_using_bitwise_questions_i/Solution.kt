// LeetCode 3064 - Guess the Number Using Bitwise Questions I
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/

/**
 * Definition of commonSetBits API.
 * fun commonSetBits(num: Int): Int
 */

class Solution : Guess() {
    fun findNumber(): Int {
        var n = 0
        for (i in 0 until 32) {
            if (commonSetBits(1 shl i) > 0) n = n or (1 shl i)
        }
        return n
    }
}
