// LeetCode 0374 - Guess Number Higher or Lower

// https://leetcode.com/problems/guess-number-higher-or-lower/

// The guess API is patched by the test runner.



def guess(num: Int): Int = 0



object Solution {

  def guessNumber(n: Int): Int = {

    var left = 1

    var right = n



    while (left <= right) {

      val mid = left + (right - left) / 2

      guess(mid) match {

        case 0 => return mid

        case -1 => right = mid - 1

        case _ => left = mid + 1

      }

    }



    left

  }

}
