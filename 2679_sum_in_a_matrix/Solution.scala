// LeetCode 2679 - Sum in a Matrix
// https://leetcode.com/problems/sum-in-a-matrix/

object Solution {
  def matrixSum(nums: Array[Array[Int]]): Int = {
    var i = 0
    while (i < nums.length) {
      scala.util.Sorting.quickSort(nums(i))
      i += 1
    }
    var ans = 0
    val n = nums(0).length
    var j = 0
    while (j < n) {
      var mx = 0
      i = 0
      while (i < nums.length) {
        mx = math.max(mx, nums(i)(j))
        i += 1
      }
      ans += mx
      j += 1
    }
    ans
  }
}
