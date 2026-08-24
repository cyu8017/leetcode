// LeetCode 3362 - Zero Array Transformation III
// https://leetcode.com/problems/zero-array-transformation-iii/

object Solution {
  def maxRemoval(nums: Array[Int], queries: Array[Array[Int]]): Int = {
    val qs = queries.sortBy(_(0))
    val h = new java.util.PriorityQueue[Int]((a: Int, b: Int) => Integer.compare(b, a))
    val n = nums.length
    val diff = new Array[Int](n + 1)
    var j = 0
    var used = 0
    var cur = 0
    var i = 0
    while (i < n) {
      cur += diff(i)
      while (j < qs.length && qs(j)(0) == i) {
        h.offer(qs(j)(1))
        j += 1
      }
      while (cur < nums(i)) {
        if (h.isEmpty || h.peek() < i) return -1
        val r = h.poll()
        cur += 1
        diff(r + 1) -= 1
        used += 1
      }
      i += 1
    }
    qs.length - used
  }
}
