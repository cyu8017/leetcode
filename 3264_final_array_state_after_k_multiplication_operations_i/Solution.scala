// LeetCode 3264 - Final Array State After K Multiplication Operations I
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

object Solution {
  def getFinalState(nums: Array[Int], k: Int, multiplier: Int): Array[Int] = {
    val h = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) =>
      if (a(0) != b(0)) Integer.compare(a(0), b(0)) else Integer.compare(a(1), b(1))
    )
    var i = 0
    while (i < nums.length) {
      h.offer(Array(nums(i), i))
      i += 1
    }
    var t = 0
    while (t < k) {
      val cur = h.poll()
      val v = cur(0) * multiplier
      val idx = cur(1)
      nums(idx) = v
      h.offer(Array(v, idx))
      t += 1
    }
    nums
  }
}
