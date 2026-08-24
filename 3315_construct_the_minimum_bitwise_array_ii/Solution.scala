// LeetCode 3315 - Construct the Minimum Bitwise Array II
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

object Solution {
  def minBitwiseArray(nums: Array[Int]): Array[Int] = {
    val ans = Array.fill(nums.length)(-1)
    var i = 0
    while (i < nums.length) {
      val n = nums(i)
      if (n != 2) {
        var b = 0
        var found = false
        while (b < 31 && !found) {
          if (((n >> b) & 1) != 0) {
            val x = n ^ (1 << b)
            if ((x | (x + 1)) == n) {
              ans(i) = x
              found = true
            }
          }
          b += 1
        }
      }
      i += 1
    }
    ans
  }
}
