// LeetCode 0400 - Nth Digit

// https://leetcode.com/problems/nth-digit/



class Solution {

    fun findNthDigit(n: Int): Int {

        var remaining = n

        var digits = 1

        var count = 9

        var start = 1



        while (remaining > digits.toLong() * count) {

            remaining -= digits * count

            digits++

            count *= 10

            start *= 10

        }



        val number = start + (remaining - 1) / digits

        return number.toString()[(remaining - 1) % digits].digitToInt()

    }

}
