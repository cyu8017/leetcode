// LeetCode 2134 - Minimum Swaps to Group All 1's Together II
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

object Solution {
  def minSwaps(nums: Array[Int]): Int = {
    var ones = 0
    nums.foreach(ones += _)
    if (ones == 0) return 0
    val n = nums.length
    var window = 0
    var i = 0
    while (i < ones) {
      window += nums(i)
      i += 1
    }
    var best = window
    i = 0
    while (i < n) {
      window -= nums(i)
      window += nums((i + ones) % n)
      best = math.max(best, window)
      i += 1
    }
    ones - best
  }
}
