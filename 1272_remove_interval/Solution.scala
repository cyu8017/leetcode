// LeetCode 1272 - Remove Interval
// https://leetcode.com/problems/remove-interval/

object Solution {
  def removeInterval(intervals: Array[Array[Int]], toBeRemoved: Array[Int]): List[List[Int]] = {
    val left = toBeRemoved(0)
    val right = toBeRemoved(1)
    val answer = scala.collection.mutable.ListBuffer.empty[List[Int]]
    for (iv <- intervals) {
      val start = iv(0)
      val end = iv(1)
      if (end <= left || start >= right) answer += List(start, end)
      else {
        if (start < left) answer += List(start, left)
        if (end > right) answer += List(right, end)
      }
    }
    answer.toList
  }
}
