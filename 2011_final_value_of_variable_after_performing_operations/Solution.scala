// LeetCode 2011 - Final Value of Variable After Performing Operations
// https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

object Solution {
  def finalValueAfterOperations(operations: Array[String]): Int = {
    var x = 0
    operations.foreach { op =>
      if (op.charAt(1) == '+') x += 1
      else x -= 1
    }
    x
  }
}
