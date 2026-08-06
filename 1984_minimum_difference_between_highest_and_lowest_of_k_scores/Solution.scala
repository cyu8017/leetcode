// LeetCode 1984 - Minimum Difference Between Highest and Lowest of K Scores
// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

object Solution {
  def minimumDifference(nums: Array[Int], k: Int): Int = {
    val sorted = nums.sorted
    (0 to sorted.length - k).map(i => sorted(i + k - 1) - sorted(i)).min
  }
}
