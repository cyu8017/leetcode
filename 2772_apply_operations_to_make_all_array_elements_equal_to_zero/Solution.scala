// LeetCode 2772 - Apply Operations to Make All Array Elements Equal to Zero
// https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

object Solution {
  def checkArray(nums: Array[Int], k: Int): Boolean = {
    val n = nums.length
    val diff = Array.ofDim[Int](n + 1)
    var cur = 0
    var i = 0
    while (i < n) {
      cur += diff(i)
      val need = nums(i) - cur
      if (need < 0) return false
      if (need > 0) {
        if (i + k > n) return false
        cur += need
        diff(i + k) -= need
      }
      i += 1
    }
    true
  }
}
