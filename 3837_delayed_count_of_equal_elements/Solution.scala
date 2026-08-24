// LeetCode 3837 - Delayed Count Of Equal Elements
// https://leetcode.com/problems/delayed-count-of-equal-elements/

object Solution {
  def delayedCount(nums: Array[Int], k: Int): Array[Int] = {
    val n = nums.length
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    val ans = new Array[Int](n)
    var i = n - k - 2
    while (i >= 0) {
      val key = nums(i + k + 1)
      cnt(key) = cnt.getOrElse(key, 0) + 1
      ans(i) = cnt.getOrElse(nums(i), 0)
      i -= 1
    }
    ans
  }
}
