// LeetCode 3282 - Reach End of Array With Max Score
// https://leetcode.com/problems/reach-end-of-array-with-max-score/

object Solution {
  def findMaximumScore(nums: Array[Int]): Long = {
    var ans = 0L
    var maxV = 0
    var i = 0
    while (i < nums.length - 1) {
      if (nums(i) > maxV) maxV = nums(i)
      ans += maxV
      i += 1
    }
    ans
  }
}
