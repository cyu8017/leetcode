// LeetCode 3787 - Find Diameter Endpoints Of A Tree
// https://leetcode.com/problems/find-diameter-endpoints-of-a-tree/

object Solution {
  def findSpecialNodes(n: Int, edges: Array[Array[Int]]): String = {
    val g = Array.fill(n)(new java.util.ArrayList[Integer]())
    edges.foreach { e =>
      g(e(0)).add(e(1))
      g(e(1)).add(e(0))
    }

    def bfs(start: Int): Array[Int] = {
      val dist = Array.fill(n)(-1)
      dist(start) = 0
      val q = new java.util.ArrayList[Integer]()
      q.add(start)
      var far = start
      var head = 0
      while (head < q.size()) {
        val u = q.get(head)
        if (dist(u) > dist(far)) far = u
        val it = g(u).iterator()
        while (it.hasNext) {
          val v = it.next()
          if (dist(v) == -1) {
            dist(v) = dist(u) + 1
            q.add(v)
          }
        }
        head += 1
      }
      val out = new Array[Int](n + 1)
      out(0) = far
      System.arraycopy(dist, 0, out, 1, n)
      out
    }

    val r0 = bfs(0)
    val a = r0(0)
    val r1 = bfs(a)
    val b = r1(0)
    val dist1 = java.util.Arrays.copyOfRange(r1, 1, n + 1)
    val r2 = bfs(b)
    val dist2 = java.util.Arrays.copyOfRange(r2, 1, n + 1)
    val d = dist1(b)
    val ans = Array.fill(n)('0')
    var i = 0
    while (i < n) {
      if (dist1(i) == d || dist2(i) == d) ans(i) = '1'
      i += 1
    }
    new String(ans)
  }
}
