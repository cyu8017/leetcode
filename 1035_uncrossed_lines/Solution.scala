// LeetCode 1035 - Uncrossed Lines
// https://leetcode.com/problems/uncrossed-lines/

object Solution {
  def maxUncrossedLines(nums1: Array[Int], nums2: Array[Int]): Int = {
    val m = nums1.length
    val n = nums2.length
    val dp = Array.fill(m + 1, n + 1)(0)
    for (i <- 1 to m; j <- 1 to n) {
      if (nums1(i - 1) == nums2(j - 1)) dp(i)(j) = dp(i - 1)(j - 1) + 1
      else dp(i)(j) = math.max(dp(i - 1)(j), dp(i)(j - 1))
    }
    dp(m)(n)
  }
}
