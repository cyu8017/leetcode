// LeetCode 1099 - Two Sum Less Than K
// https://leetcode.com/problems/two-sum-less-than-k/

object Solution {
  def twoSumLessThanK(nums: Array[Int], k: Int): Int = {
    val sorted = nums.sorted
    var lo = 0
    var hi = sorted.length - 1
    var ans = -1
    while (lo < hi) {
      val total = sorted(lo) + sorted(hi)
      if (total < k) { ans = math.max(ans, total); lo += 1 }
      else hi -= 1
    }
    ans
  }
}
