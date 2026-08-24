// LeetCode 0882 - Reachable Nodes In Subdivided Graph
// https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

object Solution {
  def reachableNodes(edges: Array[Array[Int]], maxMoves: Int, n: Int): Int = {
    val graph = Array.fill(n)(scala.collection.mutable.Map.empty[Int, Int])
    edges.foreach { e =>
      graph(e(0))(e(1)) = e(2)
      graph(e(1))(e(0)) = e(2)
    }
    val pq = scala.collection.mutable.PriorityQueue[(Int, Int)]()
    pq.enqueue((maxMoves, 0))
    val seen = scala.collection.mutable.Map.empty[Int, Int]
    while (pq.nonEmpty) {
      val (moves, node) = pq.dequeue()
      if (!seen.contains(node)) {
        seen(node) = moves
        graph(node).foreach { case (nei, cnt) =>
          val remain = moves - cnt - 1
          if (!seen.contains(nei) && remain >= 0) pq.enqueue((remain, nei))
        }
      }
    }
    var ans = seen.size
    edges.foreach { e =>
      val left = seen.getOrElse(e(0), 0)
      val right = seen.getOrElse(e(1), 0)
      ans += math.min(e(2), left + right)
    }
    ans
  }
}
