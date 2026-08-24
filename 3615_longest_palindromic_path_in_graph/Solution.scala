// LeetCode 3615 - Longest Palindromic Path in Graph
// https://leetcode.com/problems/longest-palindromic-path-in-graph/

object Solution {
  private def pack(a: Int, b: Int): Long =
    (a.toLong << 32) | (b.toLong & 0xffffffffL)

  private def expandPal(g: Array[java.util.List[Integer]], label: String, l: Int, r: Int): Int = {
    val vis = new java.util.HashSet[java.lang.Long]()
    val q = new java.util.ArrayDeque[Array[Int]]()
    val len0 = if (l != r) 2 else 1
    q.offer(Array(l, r, len0))
    var best = len0
    vis.add(pack(math.min(l, r), math.max(l, r)))
    while (!q.isEmpty) {
      val cur = q.poll()
      val itA = g(cur(0)).iterator()
      while (itA.hasNext) {
        val a = itA.next().intValue()
        val itB = g(cur(1)).iterator()
        while (itB.hasNext) {
          val b = itB.next().intValue()
          if (a != b && label.charAt(a) == label.charAt(b)) {
            val p = pack(math.min(a, b), math.max(a, b))
            if (!vis.contains(p)) {
              vis.add(p)
              val nl = cur(2) + 2
              best = math.max(best, nl)
              q.offer(Array(a, b, nl))
            }
          }
        }
      }
    }
    best
  }

  def maxLen(n: Int, edges: Array[Array[Int]], label: String): Int = {
    val g = Array.fill[java.util.List[Integer]](n)(new java.util.ArrayList[Integer]())
    edges.foreach { e =>
      g(e(0)).add(e(1))
      g(e(1)).add(e(0))
    }
    var ans = 1
    var i = 0
    while (i < n) {
      ans = math.max(ans, expandPal(g, label, i, i))
      val it = g(i).iterator()
      while (it.hasNext) {
        val j = it.next().intValue()
        if (i < j && label.charAt(i) == label.charAt(j))
          ans = math.max(ans, expandPal(g, label, i, j))
      }
      i += 1
    }
    ans
  }
}
