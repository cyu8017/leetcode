// LeetCode 0598 - Range Addition II
// https://leetcode.com/problems/range-addition-ii/

object Solution {
  def maxCount(m0: Int, n0: Int, ops: Array[Array[Int]]): Int = {
    var m = m0
    var n = n0
    ops.foreach { op =>
      m = math.min(m, op(0))
      n = math.min(n, op(1))
    }
    m * n
  }
}
