// LeetCode 2099 - Find Subsequence of Length K With the Largest Sum
// https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

object Solution {
  def maxSubsequence(nums: Array[Int], k: Int): Array[Int] = {
    val n = nums.length
    val arr = Array.tabulate(n)(i => (nums(i), i))
    val top = arr.sortBy(-_._1).take(k).map(_._2).sorted
    top.map(nums)
  }
}
