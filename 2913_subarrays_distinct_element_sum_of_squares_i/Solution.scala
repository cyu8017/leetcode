// LeetCode 2913 - Subarrays Distinct Element Sum of Squares I
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

object Solution {
  def sumCounts(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    for (i <- 0 until n) {
      val seen = scala.collection.mutable.Set.empty[Int]
      for (j <- i until n) {
        seen += nums(j)
        val d = seen.size
        ans += d * d
      }
    }
    ans
  }
}
