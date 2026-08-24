// LeetCode 0682 - Baseball Game
// https://leetcode.com/problems/baseball-game/

object Solution {
  def calPoints(operations: Array[String]): Int = {
    val stack = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (op <- operations) {
      if (op == "C") stack.remove(stack.length - 1)
      else if (op == "D") stack += stack.last * 2
      else if (op == "+") stack += stack.last + stack(stack.length - 2)
      else stack += op.toInt
    }
    stack.sum
  }
}
