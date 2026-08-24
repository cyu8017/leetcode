// LeetCode 0862 - Shortest Subarray with Sum at Least K
// https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

object Solution {
  def shortestSubarray(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val prefix = Array.ofDim[Long](n + 1)
    var i = 0
    while (i < n) {
      prefix(i + 1) = prefix(i) + nums(i)
      i += 1
    }
    val dq = scala.collection.mutable.ArrayDeque.empty[Int]
    var ans = n + 1
    i = 0
    while (i <= n) {
      while (dq.nonEmpty && prefix(i) - prefix(dq.head) >= k) {
        ans = math.min(ans, i - dq.removeHead())
      }
      while (dq.nonEmpty && prefix(i) <= prefix(dq.last)) dq.removeLast()
      dq.append(i)
      i += 1
    }
    if (ans <= n) ans else -1
  }
}
