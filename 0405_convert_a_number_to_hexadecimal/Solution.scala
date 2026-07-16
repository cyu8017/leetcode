// LeetCode 0405 - Convert a Number to Hexadecimal

// https://leetcode.com/problems/convert-a-number-to-hexadecimal/



object Solution {

  def toHex(num: Int): String = {

    if (num == 0) {

      return "0"

    }



    val digits = "0123456789abcdef"

    var value = num.toLong & 0xffffffffL

    val result = new StringBuilder



    while (value > 0) {

      result.append(digits.charAt((value & 15).toInt))

      value >>= 4

    }



    result.reverse().toString

  }

}
