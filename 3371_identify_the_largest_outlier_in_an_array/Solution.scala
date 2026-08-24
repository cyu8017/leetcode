// LeetCode 3371 - Identify the Largest Outlier in an Array
// https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

object Solution {
  def getLargestOutlier(nums: Array[Int]): Int = {
    var sum = 0
    val freq = scala.collection.mutable.HashMap.empty[Int, Int]
    for (x <- nums) {
      sum += x
      freq(x) = freq.getOrElse(x, 0) + 1
    }
    var ans = Int.MinValue
    for (x <- nums) {
      freq(x) = freq(x) - 1
      val rem = sum - x
      if (rem % 2 == 0) {
        val cand = rem / 2
        if (freq.getOrElse(cand, 0) > 0 && x > ans) ans = x
      }
      freq(x) = freq(x) + 1
    }
    ans
  }
}
