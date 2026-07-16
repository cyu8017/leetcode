// LeetCode 0343 - Integer Break

// https://leetcode.com/problems/integer-break/



class Solution {

    fun integerBreak(n: Int): Int {

        if (n <= 3) {

            return n - 1

        }



        var product = 1

        var remaining = n

        while (remaining > 4) {

            product *= 3

            remaining -= 3

        }

        return product * remaining

    }

}
