// LeetCode 3075 - Maximize Happiness of Selected Children
// https://leetcode.com/problems/maximize-happiness-of-selected-children/

object Solution {
  def maximumHappinessSum(happiness: Array[Int], k: Int): Long = {
    val h = happiness.sorted
    var ans = 0L
    var i = 0
    while (i < k) {
      val x = h(h.length - i - 1) - i
      ans += math.max(x, 0)
      i += 1
    }
    ans
  }
}
