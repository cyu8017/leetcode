// LeetCode 2422 - Merge Operations to Turn Array Into a Palindrome
// https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/

object Solution {
  def minimumOperations(nums: Array[Int]): Int = {
    var l = 0
    var r = nums.length - 1
    var left = nums(l).toLong
    var right = nums(r).toLong
    var ans = 0
    while (l < r) {
      if (left == right) {
        l += 1
        r -= 1
        if (l < r) {
          left = nums(l)
          right = nums(r)
        }
      } else if (left < right) {
        l += 1
        left += nums(l)
        ans += 1
      } else {
        r -= 1
        right += nums(r)
        ans += 1
      }
    }
    ans
  }
}
