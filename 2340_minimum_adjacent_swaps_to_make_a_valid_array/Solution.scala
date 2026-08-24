// LeetCode 2340 - Minimum Adjacent Swaps to Make a Valid Array
// https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/

object Solution {
  def minimumSwaps(nums: Array[Int]): Int = {
    val n = nums.length
    var minI = 0
    var maxI = 0
    var i = 1
    while (i < n) {
      if (nums(i) < nums(minI)) minI = i
      if (nums(i) >= nums(maxI)) maxI = i
      i += 1
    }
    var ans = minI + (n - 1 - maxI)
    if (minI > maxI) ans -= 1
    ans
  }
}
