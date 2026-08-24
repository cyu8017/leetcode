// LeetCode 2006 - Count Number of Pairs With Absolute Difference K
// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

object Solution {
  def countKDifference(nums: Array[Int], k: Int): Int = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    var ans = 0
    nums.foreach { x =>
      ans += freq.getOrElse(x - k, 0)
      ans += freq.getOrElse(x + k, 0)
      freq(x) = freq.getOrElse(x, 0) + 1
    }
    ans
  }
}
