// LeetCode 2508 - Add Edges to Make Degrees of All Nodes Even
// https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

object Solution {
  def isPossible(n: Int, edges: List[List[Int]]): Boolean = {
    val deg = new Array[Int](n + 1)
    val adj = Array.fill(n + 1)(scala.collection.mutable.HashSet.empty[Int])
    edges.foreach { e =>
      val u = e(0)
      val v = e(1)
      deg(u) += 1
      deg(v) += 1
      adj(u) += v
      adj(v) += u
    }
    val odd = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 1
    while (i <= n) {
      if (deg(i) % 2 == 1) odd += i
      i += 1
    }
    if (odd.isEmpty) return true
    if (odd.length == 2) {
      val a = odd(0)
      val b = odd(1)
      if (!adj(a).contains(b)) return true
      i = 1
      while (i <= n) {
        if (i != a && i != b && !adj(a).contains(i) && !adj(b).contains(i)) return true
        i += 1
      }
      return false
    }
    if (odd.length == 4) {
      val a = odd(0)
      val b = odd(1)
      val c = odd(2)
      val d = odd(3)
      return (!adj(a).contains(b) && !adj(c).contains(d)) ||
        (!adj(a).contains(c) && !adj(b).contains(d)) ||
        (!adj(a).contains(d) && !adj(b).contains(c))
    }
    false
  }
}
