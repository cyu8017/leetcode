// LeetCode 2411 - Smallest Subarrays With Maximum Bitwise OR
// https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

object Solution {
  def smallestSubarrays(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val ans = Array.fill(n)(0)
    val last = Array.fill(32)(-1)
    var i = n - 1
    while (i >= 0) {
      var b = 0
      while (b < 32) {
        if (((nums(i) >> b) & 1) != 0) last(b) = i
        b += 1
      }
      var far = i
      b = 0
      while (b < 32) {
        far = math.max(far, last(b))
        b += 1
      }
      ans(i) = far - i + 1
      i -= 1
    }
    ans
  }
}
