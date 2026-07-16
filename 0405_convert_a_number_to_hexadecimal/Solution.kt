// LeetCode 0405 - Convert a Number to Hexadecimal

// https://leetcode.com/problems/convert-a-number-to-hexadecimal/



class Solution {

    fun toHex(num: Int): String {

        if (num == 0) {

            return "0"

        }



        val digits = "0123456789abcdef"

        var value = num.toLong() and 0xffffffffL

        val result = StringBuilder()



        while (value > 0) {

            result.append(digits[(value and 15).toInt()])

            value = value shr 4

        }



        return result.reverse().toString()

    }

}
