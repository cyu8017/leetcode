// LeetCode 3462 - Maximum Sum With at Most K Elements
// https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

object Solution {
  def maxSum(grid: Array[Array[Int]], limits: Array[Int], k: Int): Long = {
    val h = new java.util.PriorityQueue[Integer]()
    var sum = 0L
    var i = 0
    while (i < grid.length) {
      val r = grid(i).clone()
      java.util.Arrays.sort(r)
      var lim = limits(i)
      if (lim > r.length) lim = r.length
      var j = 0
      while (j < lim) {
        val `val` = r(r.length - 1 - j)
        h.offer(`val`)
        sum += `val`
        if (h.size() > k) sum -= h.poll()
        j += 1
      }
      i += 1
    }
    sum
  }
}
