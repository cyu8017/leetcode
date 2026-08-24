// LeetCode 3314 - Construct the Minimum Bitwise Array I
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

object Solution {
  def minBitwiseArray(nums: Array[Int]): Array[Int] = {
    val ans = Array.fill(nums.length)(-1)
    var i = 0
    while (i < nums.length) {
      val n = nums(i)
      var x = 0
      var found = false
      while (x < n && !found) {
        if ((x | (x + 1)) == n) {
          ans(i) = x
          found = true
        }
        x += 1
      }
      i += 1
    }
    ans
  }
}
