// LeetCode 2805 - Custom Interval
// https://leetcode.com/problems/custom-interval/

object Solution {
  def customInterval(fn: () => Unit, delay: Int, period: Int): () => Unit = {
    var cancelled = false
    () => { cancelled = true }
  }
}
