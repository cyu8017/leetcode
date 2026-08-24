// LeetCode 2968 - Apply Operations to Maximize Frequency Score
// https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

object Solution {
  private def cost(nums: Array[Int], pref: Array[Long], l: Int, r: Int): Long = {
    val mid = (l + r) / 2
    val left = nums(mid).toLong * (mid - l) - (pref(mid) - pref(l))
    val right = (pref(r + 1) - pref(mid + 1)) - nums(mid).toLong * (r - mid)
    left + right
  }

  def maxFrequencyScore(nums: Array[Int], k: Long): Int = {
    scala.util.Sorting.quickSort(nums)
    val n = nums.length
    val pref = Array.ofDim[Long](n + 1)
    var i = 0
    while (i < n) { pref(i + 1) = pref(i) + nums(i); i += 1 }
    var ans = 1
    var left = 0
    var right = 0
    while (right < n) {
      while (cost(nums, pref, left, right) > k) left += 1
      ans = math.max(ans, right - left + 1)
      right += 1
    }
    ans
  }
}
