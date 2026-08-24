// LeetCode 2050 - Parallel Courses III
// https://leetcode.com/problems/parallel-courses-iii/

object Solution {
  def minimumTime(n: Int, relations: Array[Array[Int]], time: Array[Int]): Int = {
    val g = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[Int])
    val indeg = Array.ofDim[Int](n + 1)
    val dist = Array.ofDim[Int](n + 1)
    relations.foreach { e => g(e(0)) += e(1); indeg(e(1)) += 1 }
    val q = scala.collection.mutable.Queue.empty[Int]
    var i = 1
    while (i <= n) {
      dist(i) = time(i - 1)
      if (indeg(i) == 0) q.enqueue(i)
      i += 1
    }
    while (q.nonEmpty) {
      val u = q.dequeue()
      g(u).foreach { v =>
        dist(v) = math.max(dist(v), dist(u) + time(v - 1))
        indeg(v) -= 1
        if (indeg(v) == 0) q.enqueue(v)
      }
    }
    var ans = 0
    i = 1
    while (i <= n) { ans = math.max(ans, dist(i)); i += 1 }
    ans
  }
}
