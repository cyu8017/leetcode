// LeetCode 1696 - Jump Game VI
// https://leetcode.com/problems/jump-game-vi/

object Solution {
  def maxResult(nums: Array[Int], k: Int): Int = {
    val q = scala.collection.mutable.ArrayBuffer((0, nums(0)))
    for (i <- 1 until nums.length) {
      while (q.head._1 < i - k) q.remove(0)
      val score = nums(i) + q.head._2
      while (q.nonEmpty && q.last._2 <= score) q.remove(q.length - 1)
      q += ((i, score))
    }
    q.last._2
  }
}
