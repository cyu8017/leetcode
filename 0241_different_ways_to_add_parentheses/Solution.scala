// LeetCode 0241 - Different Ways to Add Parentheses
// https://leetcode.com/problems/different-ways-to-add-parentheses/

object Solution {
  def diffWaysToCompute(expression: String): List[Int] = {
    if (expression.forall(_.isDigit)) {
      List(expression.toInt)
    } else {
      val result = scala.collection.mutable.ListBuffer[Int]()
      expression.indices.foreach { index =>
        val operator = expression(index)
        if (operator == '+' || operator == '-' || operator == '*') {
          val left = diffWaysToCompute(expression.substring(0, index))
          val right = diffWaysToCompute(expression.substring(index + 1))
          for (leftValue <- left; rightValue <- right) {
            result += (operator match {
              case '+' => leftValue + rightValue
              case '-' => leftValue - rightValue
              case _   => leftValue * rightValue
            })
          }
        }
      }
      result.toList
    }
  }
}
