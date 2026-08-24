// LeetCode 2552 - Count Increasing Quadruplets
// https://leetcode.com/problems/count-increasing-quadruplets/

object Solution {
  def countQuadruplets(nums: Array[Int]): Long = {
    val n = nums.length
    var ans = 0L
    val great = Array.fill(n)(0)
    var j = 0
    while (j < n) {
      var i = 0
      while (i < j) {
        if (nums(i) < nums(j)) ans += great(i)
        else if (nums(i) > nums(j)) great(i) += 1
        i += 1
      }
      j += 1
    }
    ans
  }
}
