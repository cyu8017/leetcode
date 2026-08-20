// LeetCode 1245 - Tree Diameter
// https://leetcode.com/problems/tree-diameter/

object Solution {
  def treeDiameter(edges: Array[Array[Int]]): Int = {
    if (edges.isEmpty) return 0
    val graph = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ListBuffer[Int]]
    for (e <- edges) {
      graph.getOrElseUpdate(e(0), scala.collection.mutable.ListBuffer.empty) += e(1)
      graph.getOrElseUpdate(e(1), scala.collection.mutable.ListBuffer.empty) += e(0)
    }
    def farthest(start: Int): (Int, Int) = {
      val q = scala.collection.mutable.Queue((start, 0))
      val seen = scala.collection.mutable.Set(start)
      var last = (start, 0)
      while (q.nonEmpty) {
        last = q.dequeue()
        for (v <- graph.getOrElse(last._1, Nil) if !seen.contains(v)) {
          seen += v
          q.enqueue((v, last._2 + 1))
        }
      }
      last
    }
    val endpoint = farthest(edges(0)(0))._1
    farthest(endpoint)._2
  }
}
