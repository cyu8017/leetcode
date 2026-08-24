// LeetCode 2101 - Detonate the Maximum Bombs
// https://leetcode.com/problems/detonate-the-maximum-bombs/

object Solution {
  def maximumDetonation(bombs: Array[Array[Int]]): Int = {
    val n = bombs.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var i = 0
    while (i < n) {
      val x1 = bombs(i)(0).toLong
      val y1 = bombs(i)(1).toLong
      val r1 = bombs(i)(2).toLong
      var j = 0
      while (j < n) {
        if (i != j) {
          val dx = bombs(j)(0) - x1
          val dy = bombs(j)(1) - y1
          if (dx * dx + dy * dy <= r1 * r1) g(i) += j
        }
        j += 1
      }
      i += 1
    }
    var ans = 0
    i = 0
    while (i < n) {
      val vis = Array.fill(n)(false)
      val q = scala.collection.mutable.Queue[Int](i)
      vis(i) = true
      var cnt = 0
      while (q.nonEmpty) {
        val u = q.dequeue()
        cnt += 1
        g(u).foreach { v =>
          if (!vis(v)) {
            vis(v) = true
            q.enqueue(v)
          }
        }
      }
      ans = math.max(ans, cnt)
      i += 1
    }
    ans
  }
}
