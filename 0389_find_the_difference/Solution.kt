// LeetCode 0389 - Find the Difference

// https://leetcode.com/problems/find-the-difference/



class Solution {

    fun findTheDifference(s: String, t: String): Char {

        var xorValue = 0

        for (ch in s) {

            xorValue = xorValue xor ch.code

        }

        for (ch in t) {

            xorValue = xorValue xor ch.code

        }

        return xorValue.toChar()

    }

}
