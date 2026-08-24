// LeetCode 2602 - Minimum Operations to Make All Array Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

object Solution {
  def minOperations(nums: Array[Int], queries: Array[Int]): Array[Long] = {
    java.util.Arrays.sort(nums)
    val n = nums.length
    val pref = Array.fill(n + 1)(0L)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) + nums(i)
      i += 1
    }
    val ans = Array.fill(queries.length)(0L)
    var qi = 0
    while (qi < queries.length) {
      val q = queries(qi)
      val idx = lowerBound(nums, q)
      val left = q.toLong * idx - pref(idx)
      val right = pref(n) - pref(idx) - q.toLong * (n - idx)
      ans(qi) = left + right
      qi += 1
    }
    ans
  }

  private def lowerBound(a: Array[Int], x: Int): Int = {
    var lo = 0
    var hi = a.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (a(mid) < x) lo = mid + 1
      else hi = mid
    }
    lo
  }
}
