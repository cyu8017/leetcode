// LeetCode 3523 - Make Array Non-decreasing
// https://leetcode.com/problems/make-array-non-decreasing/

object Solution {
  def maximumPossibleSize(nums: Array[Int]): Int = {
    var ans = 0
    var mx = 0
    for (x <- nums) {
      if (mx <= x) {
        ans += 1
        mx = x
      }
    }
    ans
  }
}
