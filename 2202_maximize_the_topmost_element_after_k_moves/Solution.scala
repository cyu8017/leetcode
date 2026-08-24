// LeetCode 2202 - Maximize the Topmost Element After K Moves
// https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

object Solution {
  def maximumTop(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    if (n == 1) return if (k % 2 != 0) -1 else nums(0)
    if (k == 0) return nums(0)
    var ans = -1
    val limit = math.min(k - 1, n)
    var i = 0
    while (i < limit) {
      ans = math.max(ans, nums(i))
      i += 1
    }
    if (k < n) ans = math.max(ans, nums(k))
    ans
  }
}
