// LeetCode 2680 - Maximum OR
// https://leetcode.com/problems/maximum-or/

object Solution {
  def maximumOr(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val pref = new Array[Long](n + 1)
    val suf = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) | (nums(i).toLong & 0xffffffffL)
      i += 1
    }
    i = n - 1
    while (i >= 0) {
      suf(i) = suf(i + 1) | (nums(i).toLong & 0xffffffffL)
      i -= 1
    }
    var ans = 0L
    i = 0
    while (i < n) {
      val cur = pref(i) | (nums(i).toLong << k) | suf(i + 1)
      if (cur > ans) ans = cur
      i += 1
    }
    ans
  }
}
