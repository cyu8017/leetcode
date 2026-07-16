// LeetCode 0415 - Add Strings

// https://leetcode.com/problems/add-strings/



object Solution {

  def addStrings(num1: String, num2: String): String = {

    var index1 = num1.length - 1

    var index2 = num2.length - 1

    var carry = 0

    val digits = new StringBuilder



    while (index1 >= 0 || index2 >= 0 || carry != 0) {

      if (index1 >= 0) {

        carry += num1(index).asDigit

        index1 -= 1

      }



      if (index2 >= 0) {

        carry += num2(index).asDigit

        index2 -= 1

      }



      digits.append(('0' + carry % 10).toChar)

      carry /= 10

    }



    digits.reverse.toString()

  }

}
