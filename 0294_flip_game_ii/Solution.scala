// LeetCode 0294 - Flip Game II
// https://leetcode.com/problems/flip-game-ii/

import scala.collection.mutable

object Solution {
  def canWin(currentState: String): Boolean = canWinMemo(currentState, mutable.Map.empty)

  private def canWinMemo(state: String, memo: mutable.Map[String, Boolean]): Boolean = {
    memo.get(state) match {
      case Some(cached) => cached
      case None =>
        var index = 0
        while (index < state.length - 1) {
          if (state(index) == '+' && state(index + 1) == '+') {
            val nextState = state.substring(0, index) + "--" + state.substring(index + 2)
            if (!canWinMemo(nextState, memo)) {
              memo(state) = true
              return true
            }
          }
          index += 1
        }
        memo(state) = false
        false
    }
  }
}
