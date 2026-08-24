// LeetCode 2848 - Points That Intersect With Cars
// https://leetcode.com/problems/points-that-intersect-with-cars/

object Solution {
  def numberOfPoints(nums: Array[Array[Int]]): Int = {
    val cov = Array.fill(102)(0)
    nums.foreach { r =>
      for (x <- r(0) to r(1)) cov(x) = 1
    }
    cov.sum
  }
}
