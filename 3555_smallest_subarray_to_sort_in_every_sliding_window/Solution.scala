// LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
// https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

object Solution {
  def f(nums: Array[Int], i: Int, j: Int, inf: Int): Int = {
    var mi = inf
    var mx = -inf
    var l = -1
    var r = -1
    var p = i
    while (p <= j) {
      if (nums(p) < mx) r = p
      else mx = nums(p)
      val q = j - p + i
      if (nums(q) > mi) l = q
      else mi = nums(q)
      p += 1
    }
    if (r == -1) 0 else r - l + 1
  }

  def minSubarraySort(nums: Array[Int], k: Int): Array[Int] = {
    val inf = 1 << 30
    val n = nums.length
    val ans = new Array[Int](n - k + 1)
    var i = 0
    while (i <= n - k) {
      ans(i) = f(nums, i, i + k - 1, inf)
      i += 1
    }
    ans
  }
}
