// LeetCode 1911 - Maximum Alternating Subsequence Sum
// https://leetcode.com/problems/maximum-alternating-subsequence-sum/

object Solution {
  def maxAlternatingSum(nums: Array[Int]): Long = {
    var even = 0L
    var odd = 0L
    for (x <- nums) {
      val ne = math.max(even, odd + x)
      val no = math.max(odd, even - x)
      even = ne
      odd = no
    }
    even
  }
}
