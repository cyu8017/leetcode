// LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

object Solution {
  private def depth(x0: Long): Int = {
    if (x0 == 1) return 0
    var x = x0
    var d = 0
    while (x > 1) {
      x = java.lang.Long.bitCount(x).toLong
      d += 1
    }
    d
  }

  def popcountDepth(nums: Array[Long], queries: Array[Array[Long]]): Array[Int] = {
    val a = nums.clone()
    val ans = new java.util.ArrayList[Integer]()
    queries.foreach { q =>
      if (q(0) == 1) {
        val l = q(1).toInt
        val r = q(2).toInt
        val k = q(3).toInt
        var cnt = 0
        var i = l
        while (i <= r) {
          if (depth(a(i)) == k) cnt += 1
          i += 1
        }
        ans.add(cnt)
      } else {
        a(q(1).toInt) = q(2)
      }
    }
    val res = new Array[Int](ans.size())
    var i = 0
    while (i < ans.size()) {
      res(i) = ans.get(i)
      i += 1
    }
    res
  }
}
