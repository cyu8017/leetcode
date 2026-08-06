// LeetCode 1562 - Find Latest Group of Size M
// https://leetcode.com/problems/find-latest-group-of-size-m/

object Solution {
  def findLatestStep(arr: Array[Int], m: Int): Int = {
    if (m == arr.length) return m
    val lengths = scala.collection.mutable.Map.empty[Int, Int]
    var answer = -1
    for ((x, step) <- arr.zipWithIndex.map { case (v, i) => (v, i + 1) }) {
      val left = lengths.getOrElse(x - 1, 0)
      val right = lengths.getOrElse(x + 1, 0)
      val size = left + 1 + right
      lengths(x - left) = size
      lengths(x + right) = size
      if (left == m || right == m) answer = step - 1
    }
    answer
  }
}
