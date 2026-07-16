// LeetCode 0293 - Flip Game
// https://leetcode.com/problems/flip-game/

import scala.collection.mutable

object Solution {
  def generatePossibleNextMoves(currentState: String): List[String] = {
    val result = mutable.ListBuffer.empty[String]
    var index = 0
    while (index < currentState.length - 1) {
      if (currentState(index) == '+' && currentState(index + 1) == '+') {
        result += currentState.substring(0, index) + "--" + currentState.substring(index + 2)
      }
      index += 1
    }
    result.toList
  }
}
