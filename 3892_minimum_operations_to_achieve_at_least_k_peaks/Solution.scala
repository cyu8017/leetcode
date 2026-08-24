// LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
// https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

object Solution {
  private var cost: Array[Long] = _
  private val INF = 1L << 60

  def minOperations(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    if (k == 0) return 0
    if (k > n / 2) return -1
    cost = new Array[Long](n)
    var i = 0
    while (i < n) {
      val left = nums((i + n - 1) % n)
      val right = nums((i + 1) % n)
      val need = math.max(left, right)
      if (need >= nums(i)) cost(i) = need.toLong - nums(i) + 1
      i += 1
    }
    var answer = line(1, n - 1, k)
    var withFirst = line(2, n - 2, k - 1)
    if (withFirst != INF) {
      withFirst += cost(0)
      answer = math.min(answer, withFirst)
    }
    if (answer == INF) -1 else answer
  }

  private def line(left: Int, right: Int, choose: Int): Long = {
    if (choose == 0) return 0
    if (left > right || choose > (right - left + 2) / 2) return INF
    var prev2 = Array.fill(choose + 1)(INF)
    var prev1 = Array.fill(choose + 1)(INF)
    prev2(0) = 0
    prev1(0) = 0
    var i = left
    while (i <= right) {
      val current = prev1.clone()
      var j = 1
      while (j <= choose) {
        if (prev2(j - 1) != INF && prev2(j - 1) + cost(i) < current(j)) {
          current(j) = prev2(j - 1) + cost(i)
        }
        j += 1
      }
      prev2 = prev1
      prev1 = current
      i += 1
    }
    prev1(choose)
  }
}
