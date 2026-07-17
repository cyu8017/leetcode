// LeetCode 1769 - Minimum Number of Operations to Move All Balls to Each Box
// https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

object Solution {
  def minOperations(boxes: String): Array[Int] = {
    val n = boxes.length
    val ans = new Array[Int](n)
    var balls = 0
    var ops = 0
    for (i <- 1 until n) {
      balls += boxes(i - 1) - '0'
      ops += balls
      ans(i) = ops
    }
    balls = 0
    ops = 0
    for (i <- (n - 2) to 0 by -1) {
      balls += boxes(i + 1) - '0'
      ops += balls
      ans(i) += ops
    }
    ans
  }
}
