// LeetCode 3134 - Find the Median of the Uniqueness Array
// https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

object Solution {
  def medianOfUniquenessArray(nums: Array[Int]): Int = {
    val n = nums.length
    val m = (1L + n) * n / 2
    var lo = 1
    var hi = n
    while (lo < hi) {
      val mid = lo + (hi - lo) / 2
      if (check(nums, n, m, mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def check(nums: Array[Int], n: Int, m: Long, mx: Int): Boolean = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var l = 0
    var k = 0L
    var r = 0
    while (r < n) {
      cnt(nums(r)) = cnt.getOrElse(nums(r), 0) + 1
      while (cnt.size > mx) {
        val y = nums(l)
        l += 1
        val nv = cnt(y) - 1
        if (nv == 0) cnt.remove(y)
        else cnt(y) = nv
      }
      k += r - l + 1
      if (k >= (m + 1) / 2) return true
      r += 1
    }
    false
  }
}
