// LeetCode 0464 - Can I Win
// https://leetcode.com/problems/can-i-win/

import scala.collection.mutable

object Solution {
  def canIWin(maxChoosableInteger: Int, desiredTotal: Int): Boolean = {
    if (desiredTotal <= 0) {
      return true
    }
    val total = maxChoosableInteger * (maxChoosableInteger + 1) / 2
    if (total < desiredTotal) {
      return false
    }

    val memo = mutable.Map.empty[Int, Boolean]
    canWin(0, 0, maxChoosableInteger, desiredTotal, memo)
  }

  private def canWin(
      state: Int,
      currentTotal: Int,
      maxChoosableInteger: Int,
      desiredTotal: Int,
      memo: mutable.Map[Int, Boolean],
  ): Boolean = {
    memo.get(state) match {
      case Some(cached) => cached
      case None =>
        var result = false
        var pick = 1
        while (pick <= maxChoosableInteger && !result) {
          val bit = 1 << (pick - 1)
          if ((state & bit) == 0) {
            if (currentTotal + pick >= desiredTotal) {
              result = true
            } else if (!canWin(state | bit, currentTotal + pick, maxChoosableInteger, desiredTotal, memo)) {
              result = true
            }
          }
          pick += 1
        }
        memo(state) = result
        result
    }
  }
}
