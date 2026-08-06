// LeetCode 1971 - Find if Path Exists in Graph
// https://leetcode.com/problems/find-if-path-exists-in-graph/

object Solution {
  def validPath(n: Int, edges: Array[Array[Int]], source: Int, destination: Int): Boolean = {
    if (source == destination) return true
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val stack = scala.collection.mutable.ArrayBuffer(source)
    val seen = scala.collection.mutable.Set(source)
    while (stack.nonEmpty) {
      val u = stack.remove(stack.length - 1)
      if (u == destination) return true
      for (v <- g(u) if !seen.contains(v)) {
        seen += v
        stack += v
      }
    }
    false
  }
}
