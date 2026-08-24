// LeetCode 0775 - Global and Local Inversions
// https://leetcode.com/problems/global-and-local-inversions/

object Solution {
  def isIdealPermutation(nums: Array[Int]): Boolean = {
    var i = 0
    while (i < nums.length) {
      if (math.abs(nums(i) - i) > 1) return false
      i += 1
    }
    true
  }
}
