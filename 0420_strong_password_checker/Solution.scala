// LeetCode 0420 - Strong Password Checker

// https://leetcode.com/problems/strong-password-checker/



object Solution {

  def strongPasswordChecker(password: String): Int = {

    val length = password.length

    var missing = 3



    if (password.exists(_.isLower)) {

      missing -= 1

    }



    if (password.exists(_.isUpper)) {

      missing -= 1

    }



    if (password.exists(_.isDigit)) {

      missing -= 1

    }



    var replace = 0

    var oneRepeat = 0

    var twoRepeat = 0

    var index = 0



    while (index < length) {

      var run = 1



      while (index + run < length && password(index + run) == password(index)) {

        run += 1

      }



      if (run >= 3) {

        replace += run / 3



        if (run % 3 == 0) {

          oneRepeat += 1

        } else if (run % 3 == 1) {

          twoRepeat += 1

        }

      }



      index += run

    }



    if (length < 6) {

      return math.max(6 - length, missing)

    }



    if (length <= 20) {

      return math.max(missing, replace)

    }



    var delete = length - 20

    replace -= math.min(delete, oneRepeat)

    delete -= math.min(delete, oneRepeat)

    replace -= math.min(delete / 2, twoRepeat)

    delete -= math.min(delete / 2, twoRepeat) * 2

    replace -= delete / 3



    length - 20 + math.max(missing, replace)

  }

}
