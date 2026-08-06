import scala.collection.mutable
object Solution {
  def minTime(n: Int, edges: Array[Array[Int]], hasApple: List[Boolean]): Int = {
    val graph = Array.fill(n)(mutable.ArrayBuffer.empty[Int])
    for (edge <- edges) { graph(edge(0)) += edge(1); graph(edge(1)) += edge(0) }
    def visit(node: Int, parent: Int): Int = graph(node).filter(_ != parent).map { child =>
      val cost = visit(child, node)
      if (cost > 0 || hasApple(child)) cost + 2 else 0
    }.sum
    visit(0, -1)
  }
}
