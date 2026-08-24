// LeetCode 3388 - Count Beautiful Splits in an Array
// https://leetcode.com/problems/count-beautiful-splits-in-an-array/

object Solution {
  private def equal(a: Array[Int], as: Int, ae: Int, b: Array[Int], bs: Int, be: Int): Boolean = {
    if (ae - as != be - bs) return false
    var i = 0
    while (i < ae - as) {
      if (a(as + i) != b(bs + i)) return false
      i += 1
    }
    true
  }

  def beautifulSplits(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    var i = 1
    while (i < n - 1) {
      var j = i + 1
      while (j < n) {
        var ok = false
        if (i <= j - i && equal(nums, 0, i, nums, i, i + i)) ok = true
        if (!ok && j - i <= n - j && equal(nums, i, j, nums, j, j + (j - i))) ok = true
        if (ok) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
