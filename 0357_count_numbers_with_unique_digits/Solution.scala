// LeetCode 0357 - Count Numbers with Unique Digits

// https://leetcode.com/problems/count-numbers-with-unique-digits/



object Solution {

  def countNumbersWithUniqueDigits(n: Int): Int = {

    if (n == 0) {

      1

    } else {

      var total = 10

      var unique = 9

      var available = 9



      for (length <- 2 to n) {

        unique *= available

        available -= 1

        total += unique

      }



      total

    }

  }

}
