// LeetCode 3887 - Incremental Even-Weighted Cycle Queries
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

object Solution {
  private var parent: Array[Int] = _
  private var size: Array[Int] = _
  private var parity: Array[Int] = _

  private def find(x: Int): Array[Int] = {
    if (parent(x) == x) return Array(x, 0)
    val res = find(parent(x))
    val root = res(0)
    val p = res(1)
    parity(x) ^= p
    parent(x) = root
    Array(root, parity(x))
  }

  def countValidEdges(n: Int, edges: Array[Array[Int]]): Int = {
    parent = new Array[Int](n)
    size = new Array[Int](n)
    parity = new Array[Int](n)
    var i = 0
    while (i < n) {
      parent(i) = i
      size(i) = 1
      i += 1
    }
    var ans = 0
    edges.foreach { e =>
      val fu = find(e(0))
      val fv = find(e(1))
      var ru = fu(0)
      var pu = fu(1)
      var rv = fv(0)
      var pv = fv(1)
      if (ru == rv) {
        if ((pu ^ pv) == e(2)) ans += 1
      } else {
        if (size(ru) < size(rv)) {
          val t = ru; ru = rv; rv = t
          val t2 = pu; pu = pv; pv = t2
        }
        parent(rv) = ru
        parity(rv) = pu ^ pv ^ e(2)
        size(ru) += size(rv)
        ans += 1
      }
    }
    ans
  }
}
