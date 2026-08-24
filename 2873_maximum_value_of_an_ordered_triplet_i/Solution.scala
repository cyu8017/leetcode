// LeetCode 2873 - Maximum Value of an Ordered Triplet I
// https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

object Solution {
  def maximumTripletValue(nums: Array[Int]): Long = {
    val n = nums.length
    var ans = 0L
    for (i <- 0 until n; j <- i + 1 until n; k <- j + 1 until n) {
      val cand = 1L * (nums(i) - nums(j)) * nums(k)
      if (cand > ans) ans = cand
    }
    ans
  }
}
