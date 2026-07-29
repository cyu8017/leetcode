// LeetCode 1051 - Height Checker
// https://leetcode.com/problems/height-checker/

object Solution {
  def heightChecker(heights: Array[Int]): Int = {
    val sorted = heights.sorted
    heights.indices.count(i => heights(i) != sorted(i))
  }
}
