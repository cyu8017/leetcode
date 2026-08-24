// LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

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
    val freq = scala.collection.mutable.HashMap.empty[Int, Int]
    for (x <- nums) freq(x) = freq.getOrElse(x, 0) + 1
    var ans = 1
    val candidates = scala.collection.mutable.ArrayBuffer.empty[Int]
    val seen = scala.collection.mutable.HashSet.empty[Int]
    for (x <- nums) {
      for (t <- Array(x - k, x, x + k)) {
        if (seen.add(t)) candidates += t
      }
    }
    for (t <- candidates) {
      val lo = lowerBound(nums, t - k)
      val hi = upperBound(nums, t + k)
      val can = hi - lo
      val f = freq.getOrElse(t, 0)
      val use = math.min(can, f + numOperations)
      if (use > ans) ans = use
    }
    ans
  }
}
