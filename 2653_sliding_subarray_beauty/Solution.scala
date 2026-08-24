// LeetCode 2653 - Sliding Subarray Beauty
// https://leetcode.com/problems/sliding-subarray-beauty/

object Solution {
  def getSubarrayBeauty(nums: Array[Int], k: Int, x: Int): Array[Int] = {
    val freq = new Array[Int](101)
    val ans = new Array[Int](nums.length - k + 1)
    var i = 0
    while (i < nums.length) {
      freq(nums(i) + 50) += 1
      if (i >= k) freq(nums(i - k) + 50) -= 1
      if (i >= k - 1) {
        var need = x
        var `val` = 0
        var j = 0
        var found = false
        while (j < 50 && !found) {
          need -= freq(j)
          if (need <= 0) {
            `val` = j - 50
            found = true
          }
          j += 1
        }
        ans(i - k + 1) = `val`
      }
      i += 1
    }
    ans
  }
}
