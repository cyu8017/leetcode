// LeetCode 2856 - Minimum Array Length After Pair Removals
// https://leetcode.com/problems/minimum-array-length-after-pair-removals/

object Solution {
  def minLengthAfterRemovals(nums: Array[Int]): Int = {
    val n = nums.length
    var mx = 0
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    nums.foreach { v =>
      freq(v) = freq.getOrElse(v, 0) + 1
      mx = math.max(mx, freq(v))
    }
    if (mx <= n / 2) n % 2 else 2 * mx - n
  }
}
