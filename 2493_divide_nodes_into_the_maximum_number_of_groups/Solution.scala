// LeetCode 2493 - Divide Nodes Into the Maximum Number of Groups
// https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

object Solution {
  def magnificentSets(n: Int, edges: Array[Array[Int]]): Int = {
    val g = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }

    def bfsDepth(start: Int): Int = {
      val dist = Array.fill(n + 1)(-1)
      val q = scala.collection.mutable.Queue[Int]()
      q.enqueue(start)
      dist(start) = 1
      var best = 1
      while (q.nonEmpty) {
        val u = q.dequeue()
        if (dist(u) > best) best = dist(u)
        g(u).foreach { v =>
          if (dist(v) == -1) {
            dist(v) = dist(u) + 1
            q.enqueue(v)
          }
        }
      }
      best
    }

    val color = Array.fill(n + 1)(-1)
    val components = scala.collection.mutable.ArrayBuffer.empty[scala.collection.mutable.ArrayBuffer[Int]]
    var i = 1
    while (i <= n) {
      if (color(i) == -1) {
        val comp = scala.collection.mutable.ArrayBuffer.empty[Int]
        val q = scala.collection.mutable.Queue[Int]()
        q.enqueue(i)
        color(i) = 0
        var bipartite = true
        while (q.nonEmpty) {
          val u = q.dequeue()
          comp += u
          g(u).foreach { v =>
            if (color(v) == -1) {
              color(v) = color(u) ^ 1
              q.enqueue(v)
            } else if (color(v) == color(u)) {
              bipartite = false
            }
          }
        }
        if (!bipartite) return -1
        components += comp
      }
      i += 1
    }
    var ans = 0
    components.foreach { comp =>
      var best = 0
      comp.foreach { u =>
        val d = bfsDepth(u)
        if (d > best) best = d
      }
      ans += best
    }
    ans
  }
}
