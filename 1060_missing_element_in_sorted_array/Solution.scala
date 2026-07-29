// LeetCode 1060 - Missing Element in Sorted Array
// https://leetcode.com/problems/missing-element-in-sorted-array/

object Solution {
  def missingElement(nums: Array[Int], k: Int): Int = {
    def missing(i: Int): Int = nums(i) - nums(0) - i
    val n = nums.length
    if (k > missing(n - 1)) return nums(n - 1) + k - missing(n - 1)
    var lo = 0
    var hi = n - 1
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (missing(mid) < k) lo = mid + 1 else hi = mid
    }
    nums(lo - 1) + k - missing(lo - 1)
  }
}
