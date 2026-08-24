// LeetCode 2780 - Minimum Index of a Valid Split
// https://leetcode.com/problems/minimum-index-of-a-valid-split/

object Solution {
  def minimumIndex(nums: List[Int]): Int = {
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    var dom = 0
    var best = 0
    nums.foreach { v =>
      val c = freq.getOrElse(v, 0) + 1
      freq(v) = c
      if (c > best) {
        best = c
        dom = v
      }
    }
    var left = 0
    val n = nums.length
    var i = 0
    while (i < n - 1) {
      if (nums(i) == dom) left += 1
      val right = best - left
      if (left * 2 > i + 1 && right * 2 > n - i - 1) return i
      i += 1
    }
    -1
  }
}
