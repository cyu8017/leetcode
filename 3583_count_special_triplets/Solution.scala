// LeetCode 3583 - Count Special Triplets
// https://leetcode.com/problems/count-special-triplets/

object Solution {
  def specialTriplets(nums: Array[Int]): Int = {
    val left = scala.collection.mutable.HashMap.empty[Int, Int]
    val right = scala.collection.mutable.HashMap.empty[Int, Int]
    for (x <- nums) right(x) = right.getOrElse(x, 0) + 1
    var ans = 0L
    val mod = 1000000007L
    for (x <- nums) {
      right(x) = right(x) - 1
      val lv = left.getOrElse(x * 2, 0).toLong
      val rv = right.getOrElse(x * 2, 0).toLong
      ans = (ans + lv * rv % mod) % mod
      left(x) = left.getOrElse(x, 0) + 1
    }
    ans.toInt
  }
}
