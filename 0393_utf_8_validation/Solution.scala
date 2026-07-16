// LeetCode 0393 - UTF-8 Validation

// https://leetcode.com/problems/utf-8-validation/



object Solution {

  def validUtf8(data: Array[Int]): Boolean = {

    var remaining = 0



    for (value <- data) {

      val byteValue = value & 0xFF



      if (remaining == 0) {

        if ((byteValue >> 7) == 0) {

        } else if ((byteValue >> 5) == 0b110) {

          remaining = 1

        } else if ((byteValue >> 4) == 0b1110) {

          remaining = 2

        } else if ((byteValue >> 3) == 0b11110) {

          remaining = 3

        } else {

          return false

        }

      } else {

        if ((byteValue >> 6) != 0b10) {

          return false

        }

        remaining -= 1

      }

    }



    remaining == 0

  }

}
