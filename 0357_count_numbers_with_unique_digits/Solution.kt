// LeetCode 0357 - Count Numbers with Unique Digits

// https://leetcode.com/problems/count-numbers-with-unique-digits/



class Solution {

    fun countNumbersWithUniqueDigits(n: Int): Int {

        if (n == 0) {

            return 1

        }



        var total = 10

        var unique = 9

        var available = 9



        for (length in 2..n) {

            unique *= available

            available--

            total += unique

        }



        return total

    }

}
