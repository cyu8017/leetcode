// LeetCode 0415 - Add Strings

// https://leetcode.com/problems/add-strings/



class Solution {

    fun addStrings(num1: String, num2: String): String {

        var index1 = num1.length - 1

        var index2 = num2.length - 1

        var carry = 0

        val digits = StringBuilder()



        while (index1 >= 0 || index2 >= 0 || carry != 0) {

            if (index1 >= 0) {

                carry += num1[index1].digitToInt()

                index1--

            }



            if (index2 >= 0) {

                carry += num2[index2].digitToInt()

                index2--

            }



            digits.append('0' + carry % 10)

            carry /= 10

        }



        return digits.reverse().toString()

    }

}
