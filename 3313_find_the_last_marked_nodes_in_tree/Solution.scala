// LeetCode 3313 - Find the Last Marked Nodes in Tree
// https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

object Solution {
  def lastMarkedNodes(edges: Array[Array[Int]]): Array[Int] = {
    val n = edges.length + 1
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    def bfs(start: Int): (Int, Array[Int]) = {
      val dist = Array.fill(n)(-1)
      val q = scala.collection.mutable.Queue[Int]()
      q.enqueue(start)
      dist(start) = 0
      var far = start
      while (q.nonEmpty) {
        val u = q.dequeue()
        if (dist(u) > dist(far)) far = u
        for (v <- g(u)) {
          if (dist(v) == -1) {
            dist(v) = dist(u) + 1
            q.enqueue(v)
          }
        }
      }
      (far, dist)
    }
    val u = bfs(0)._1
    val (v, du) = bfs(u)
    val dv = bfs(v)._2
    Array.tabulate(n)(i => if (du(i) >= dv(i)) u else v)
  }
}
