// LeetCode 3493 - Properties Graph
// https://leetcode.com/problems/properties-graph/

object Solution {
  private var parent: Array[Int] = _

  private def find(x0: Int): Int = {
    var x = x0
    if (parent(x) != x) parent(x) = find(parent(x))
    parent(x)
  }

  private def unite(a: Int, b: Int): Unit = {
    val ra = find(a)
    val rb = find(b)
    if (ra != rb) parent(ra) = rb
  }

  def numberOfComponents(properties: Array[Array[Int]], k: Int): Int = {
    val n = properties.length
    val sets = Array.fill(n)(scala.collection.mutable.Set.empty[Int])
    var i = 0
    while (i < n) {
      properties(i).foreach(v => sets(i) += v)
      i += 1
    }
    parent = Array.tabulate(n)(identity)
    i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        var cnt = 0
        sets(i).foreach { v => if (sets(j).contains(v)) cnt += 1 }
        if (cnt >= k) unite(i, j)
        j += 1
      }
      i += 1
    }
    val comp = scala.collection.mutable.Set.empty[Int]
    i = 0
    while (i < n) { comp += find(i); i += 1 }
    comp.size
  }
}
