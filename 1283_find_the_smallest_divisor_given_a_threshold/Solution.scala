// LeetCode 1283 - Find the Smallest Divisor Given a Threshold
// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

object Solution {
  def smallestDivisor(nums: Array[Int], threshold: Int): Int = {
    var lo = 1
    var hi = nums.max
    while (lo < hi) {
      val mid = (lo + hi) / 2
      val total = nums.map(x => (x + mid - 1) / mid).sum
      if (total <= threshold) hi = mid else lo = mid + 1
    }
    lo
  }
}
