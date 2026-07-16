// LeetCode 0338 - Counting Bits

// https://leetcode.com/problems/counting-bits/



class Solution {

    fun countBits(n: Int): IntArray {

        val result = IntArray(n + 1)

        for (index in 1..n) {

            result[index] = result[index and (index - 1)] + 1

        }

        return result

    }

}
