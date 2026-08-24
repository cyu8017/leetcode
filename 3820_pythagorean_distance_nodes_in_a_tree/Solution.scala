// LeetCode 3820 - Pythagorean Distance Nodes In A Tree
// https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/

object Solution {
  def specialNodes(n: Int, edges: Array[Array[Int]], x: Int, y: Int, z: Int): Int = {
    val g = Array.fill(n)(new java.util.ArrayList[Integer]())
    edges.foreach { e =>
      g(e(0)).add(e(1))
      g(e(1)).add(e(0))
    }

    def bfs(start: Int): Array[Int] = {
      val dist = Array.fill(n)(1000000000)
      val q = new java.util.ArrayDeque[Integer]()
      dist(start) = 0
      q.offer(start)
      while (!q.isEmpty) {
        val u = q.poll()
        val it = g(u).iterator()
        while (it.hasNext) {
          val v = it.next()
          if (dist(v) > dist(u) + 1) {
            dist(v) = dist(u) + 1
            q.offer(v)
          }
        }
      }
      dist
    }

    val d1 = bfs(x)
    val d2 = bfs(y)
    val d3 = bfs(z)
    var ans = 0
    var i = 0
    while (i < n) {
      val a = Array(d1(i), d2(i), d3(i))
      java.util.Arrays.sort(a)
      val x0 = a(0).toLong
      val x1 = a(1).toLong
      val x2 = a(2).toLong
      if (x0 * x0 + x1 * x1 == x2 * x2) ans += 1
      i += 1
    }
    ans
  }
}
