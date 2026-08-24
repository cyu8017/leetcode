// LeetCode 3919 - Minimum Cost To Move Between Indices
// https://leetcode.com/problems/minimum-cost-to-move-between-indices/

object Solution {
  def minCost(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = nums.length
    val s1 = new Array[Int](n)
    val s2 = new Array[Int](n)
    var i = 1
    while (i < n) {
      var c1 = 1
      if (i > 1 && nums(i - 1) - nums(i - 2) <= nums(i) - nums(i - 1)) c1 = nums(i) - nums(i - 1)
      var c2 = 1
      if (i < n - 1 && nums(i) - nums(i - 1) > nums(i + 1) - nums(i)) c2 = nums(i) - nums(i - 1)
      s1(i) = s1(i - 1) + c1
      s2(i) = s2(i - 1) + c2
      i += 1
    }
    val ans = new Array[Int](queries.length)
    i = 0
    while (i < queries.length) {
      val l = queries(i)(0)
      val r = queries(i)(1)
      ans(i) = if (l < r) s1(r) - s1(l) else s2(l) - s2(r)
      i += 1
    }
    ans
  }
}
