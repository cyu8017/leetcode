// LeetCode 0326 - Power of Three

// https://leetcode.com/problems/power-of-three/



class Solution {

    fun isPowerOfThree(n: Int): Boolean {

        if (n <= 0) {

            return false

        }

        var value = n

        while (value % 3 == 0) {

            value /= 3

        }

        return value == 1

    }

}

