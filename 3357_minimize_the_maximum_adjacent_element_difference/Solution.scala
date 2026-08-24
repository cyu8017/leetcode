// LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
// https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

object Solution {
  def minDifference(nums: Array[Int]): Int = {
    val n = nums.length
    var lo = 0
    var hi = 1000000000
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(mid, nums, n)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def ok(d: Int, nums: Array[Int], n: Int): Boolean = {
    var prev = -1
    var i = 0
    while (i < n) {
      if (nums(i) != -1) {
        if (prev != -1 && math.abs(nums(i) - prev) > d) return false
        prev = nums(i)
      } else {
        var j = i
        while (j < n && nums(j) == -1) j += 1
        val left = prev
        val right = if (j < n) nums(j) else -1
        val gap = j - i
        if (left == -1 && right == -1) return true
        if (left == -1 || right == -1) {
          prev = -1
          i = j - 1
        } else {
          if (math.abs(left - right) > d.toLong * (gap + 1)) return false
          prev = -1
          i = j - 1
        }
      }
      i += 1
    }
    true
  }
}
