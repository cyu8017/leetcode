// LeetCode 3623 - Count Number of Trapezoids I
// https://leetcode.com/problems/count-number-of-trapezoids-i/

object Solution {
  def countTrapezoids(points: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val cnt = new java.util.HashMap[Integer, Integer]()
    points.foreach { p =>
      cnt.merge(p(1), 1, Integer.sum)
    }
    var ans = 0L
    var pre = 0L
    val it = cnt.values().iterator()
    while (it.hasNext) {
      val c = it.next().intValue()
      val lines = c.toLong * (c - 1) / 2
      ans = (ans + pre * lines) % MOD
      pre = (pre + lines) % MOD
    }
    ans.toInt
  }
}
