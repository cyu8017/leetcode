// LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

object Solution {
  private def lowerBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) < x) lo = mid + 1 else hi = mid
    }
    lo
  }
  private def upperBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) <= x) lo = mid + 1 else hi = mid
    }
    lo
  }

  def maxFrequency(nums: Array[Int], k: Int, numOperations: Int): Int = {
    scala.util.Sorting.quickSort(nums)
    val n = nums.length
    val freq = scala.collection.mutable.HashMap.empty[Int, Int]
    for (x <- nums) freq(x) = freq.getOrElse(x, 0) + 1
    var ans = 1
    for ((t, f) <- freq) {
      val lo = lowerBound(nums, t - k)
      val hi = upperBound(nums, t + k)
      val can = hi - lo
      val use = math.min(can, f + numOperations)
      if (use > ans) ans = use
    }
    var l = 0
    var r = 0
    while (r < n) {
      while (nums(r) - nums(l) > 2 * k) l += 1
      val window = math.min(r - l + 1, numOperations)
      if (window > ans) ans = window
      r += 1
    }
    ans
  }
}
