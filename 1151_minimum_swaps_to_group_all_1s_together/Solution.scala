// LeetCode 1151 - Minimum Swaps to Group All 1's Together
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

object Solution {
  def minSwaps(data: Array[Int]): Int = {
    val ones = data.sum
    if (ones <= 1) return 0
    var cur = data.take(ones).sum
    var best = cur
    for (i <- ones until data.length) {
      cur += data(i) - data(i - ones)
      best = math.max(best, cur)
    }
    ones - best
  }
}
