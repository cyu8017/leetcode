object Solution {
  def frogPosition(n: Int, edges: Array[Array[Int]], t: Int, target: Int): Double = {
    val graph = Array.fill(n + 1)(collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach(edge => { graph(edge(0)) += edge(1); graph(edge(1)) += edge(0) })
    def dfs(node: Int, parent: Int, time: Int, probability: Double): Double = {
      val children = graph(node).filter(_ != parent)
      if (time == t || children.isEmpty) if (node == target) probability else 0.0
      else children.map(child => dfs(child, node, time + 1, probability / children.length)).sum
    }
    dfs(1, 0, 0, 1.0)
  }
}
