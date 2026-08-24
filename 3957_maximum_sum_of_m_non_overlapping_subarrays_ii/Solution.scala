// LeetCode 3957 - Maximum Sum of M Non-Overlapping Subarrays II
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/

import scala.collection.mutable

object Solution {
  private class State(var value: Long = 0, var count: Int = 0)

  private def better(a: State, b: State): Boolean =
    a.value > b.value || (a.value == b.value && a.count > b.count)

  def maxSum(nums: Array[Int], m: Int, l: Int, r: Int): Long = {
    val n = nums.length
    val prefix = new Array[Long](n + 1)
    var i = 0
    while (i < n) {
      prefix(i + 1) = prefix(i) + nums(i)
      i += 1
    }
    val unconstrained = run(prefix, n, l, r, 0)
    if (unconstrained.count > 0 && unconstrained.count <= m) return unconstrained.value
    if (unconstrained.count > m) {
      var bound = 0L
      for (value <- nums) bound += (if (value >= 0) value else -value)
      var low = 0L
      var high = bound + 1
      while (low < high) {
        val mid = low + (high - low + 1) / 2
        if (run(prefix, n, l, r, mid).count >= m) low = mid
        else high = mid - 1
      }
      val state = run(prefix, n, l, r, low)
      return state.value + low * m
    }
    val infinity = 1L << 60
    var bestSingle = -infinity
    val deque = mutable.ArrayDeque[Int]()
    var end = 1
    while (end <= n) {
      val addIndex = end - l
      if (addIndex >= 0) {
        while (deque.nonEmpty && prefix(deque.last) >= prefix(addIndex)) deque.removeLast()
        deque.append(addIndex)
      }
      val minIndex = end - r
      while (deque.nonEmpty && deque.head < minIndex) deque.removeHead()
      if (deque.nonEmpty) {
        val sum = prefix(end) - prefix(deque.head)
        if (sum > bestSingle) bestSingle = sum
      }
      end += 1
    }
    bestSingle
  }

  private def run(prefix: Array[Long], n: Int, l: Int, r: Int, penalty: Long): State = {
    val dp = Array.fill(n + 1)(new State())
    val deque = mutable.ArrayDeque[Int]()
    var end = 1
    while (end <= n) {
      val addIndex = end - l
      if (addIndex >= 0) {
        while (deque.nonEmpty && candidateBetter(dp, prefix, addIndex, deque.last)) deque.removeLast()
        deque.append(addIndex)
      }
      val minIndex = end - r
      while (deque.nonEmpty && deque.head < minIndex) deque.removeHead()
      dp(end) = new State(dp(end - 1).value, dp(end - 1).count)
      if (deque.nonEmpty) {
        val start = deque.head
        val take = new State(dp(start).value + prefix(end) - prefix(start) - penalty, dp(start).count + 1)
        if (better(take, dp(end))) dp(end) = take
      }
      end += 1
    }
    dp(n)
  }

  private def candidateBetter(dp: Array[State], prefix: Array[Long], a: Int, b: Int): Boolean = {
    val left = new State(dp(a).value - prefix(a), dp(a).count)
    val right = new State(dp(b).value - prefix(b), dp(b).count)
    better(left, right)
  }
}
