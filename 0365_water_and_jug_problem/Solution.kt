// LeetCode 0365 - Water and Jug Problem

// https://leetcode.com/problems/water-and-jug-problem/



class Solution {

    fun canMeasureWater(x: Int, y: Int, target: Int): Boolean {

        if (target == 0) {

            return true

        }

        if (x + y < target) {

            return false

        }

        return target % gcd(x, y) == 0

    }



    private fun gcd(a: Int, b: Int): Int {

        var x = a

        var y = b

        while (y != 0) {

            val temp = y

            y = x % y

            x = temp

        }

        return x

    }

}
