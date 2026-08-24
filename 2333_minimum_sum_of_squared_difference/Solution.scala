// LeetCode 2333 - Minimum Sum of Squared Difference
// https://leetcode.com/problems/minimum-sum-of-squared-difference/

object Solution {
  def minSumSquareDiff(nums1: Array[Int], nums2: Array[Int], k1: Int, k2: Int): Long = {
    val n = nums1.length
    val diff = Array.fill(n)(0)
    var maxD = 0
    var i = 0
    while (i < n) {
      val d = math.abs(nums1(i) - nums2(i))
      diff(i) = d
      if (d > maxD) maxD = d
      i += 1
    }
    var k = k1 + k2
    val freq = Array.fill(maxD + 1)(0)
    diff.foreach(d => freq(d) += 1)
    var d = maxD
    while (d > 0 && k > 0) {
      if (freq(d) != 0) {
        var take = freq(d)
        if (take > k) take = k
        freq(d) -= take
        freq(d - 1) += take
        k -= take
      }
      d -= 1
    }
    var ans = 0L
    d = 0
    while (d <= maxD) {
      ans += d.toLong * d * freq(d)
      d += 1
    }
    ans
  }
}
