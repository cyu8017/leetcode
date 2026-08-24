// LeetCode 2903 - Find Indices With Index and Value Difference I
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

object Solution {
  def findIndices(nums: Array[Int], indexDifference: Int, valueDifference: Int): Array[Int] = {
    val n = nums.length
    for (i <- 0 until n; j <- i until n) {
      val di = math.abs(j - i)
      val dv = math.abs(nums(i) - nums(j))
      if (di >= indexDifference && dv >= valueDifference) return Array(i, j)
    }
    Array(-1, -1)
  }
}
