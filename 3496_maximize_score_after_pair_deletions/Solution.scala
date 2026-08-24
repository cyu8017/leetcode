// LeetCode 3496 - Maximize Score After Pair Deletions
// https://leetcode.com/problems/maximize-score-after-pair-deletions/

object Solution {
  def maximizeScore(nums: Array[Int]): Int = {
    val n = nums.length
    var total = 0
    nums.foreach(x => total += x)
    if (n % 2 == 1) {
      var mn = nums(0)
      nums.foreach { x => if (x < mn) mn = x }
      return total - mn
    }
    var mn = nums(0) + nums(1)
    var i = 0
    while (i + 1 < n) {
      mn = math.min(mn, nums(i) + nums(i + 1))
      i += 1
    }
    total - mn
  }
}
