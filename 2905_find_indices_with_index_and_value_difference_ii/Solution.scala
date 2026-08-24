// LeetCode 2905 - Find Indices With Index and Value Difference II
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

object Solution {
  def findIndices(nums: Array[Int], indexDifference: Int, valueDifference: Int): Array[Int] = {
    val n = nums.length
    var minIdx = 0
    var maxIdx = 0
    for (j <- indexDifference until n) {
      val i = j - indexDifference
      if (nums(i) < nums(minIdx)) minIdx = i
      if (nums(i) > nums(maxIdx)) maxIdx = i
      if (nums(j) - nums(minIdx) >= valueDifference) return Array(minIdx, j)
      if (nums(maxIdx) - nums(j) >= valueDifference) return Array(maxIdx, j)
    }
    Array(-1, -1)
  }
}
