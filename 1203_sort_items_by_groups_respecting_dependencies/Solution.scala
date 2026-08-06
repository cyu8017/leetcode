// LeetCode 1203 - Sort Items by Groups Respecting Dependencies
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

object Solution {
  def sortItems(n: Int, m: Int, group: Array[Int], beforeItems: Array[List[Int]]): Array[Int] = {
    val grp = group.clone()
    var gm = m
    for (i <- 0 until n if grp(i) == -1) {
      grp(i) = gm
      gm += 1
    }
    val itemGraph = Array.fill(n)(scala.collection.mutable.ListBuffer.empty[Int])
    val itemIndeg = Array.fill(n)(0)
    val groupGraph = Array.fill(gm)(scala.collection.mutable.Set.empty[Int])
    val groupIndeg = Array.fill(gm)(0)
    for (v <- 0 until n; u <- beforeItems(v)) {
      itemGraph(u) += v
      itemIndeg(v) += 1
      if (grp(u) != grp(v) && !groupGraph(grp(u)).contains(grp(v))) {
        groupGraph(grp(u)) += grp(v)
        groupIndeg(grp(v)) += 1
      }
    }
    def topo(graph: Array[_ <: Iterable[Int]], indeg: Array[Int]): Array[Int] = {
      val q = scala.collection.mutable.Queue[Int]()
      for (i <- indeg.indices if indeg(i) == 0) q.enqueue(i)
      val order = scala.collection.mutable.ArrayBuffer.empty[Int]
      while (q.nonEmpty) {
        val u = q.dequeue()
        order += u
        for (v <- graph(u)) {
          indeg(v) -= 1
          if (indeg(v) == 0) q.enqueue(v)
        }
      }
      if (order.length == graph.length) order.toArray else Array.empty
    }
    val items = topo(itemGraph, itemIndeg)
    val groups = topo(groupGraph.map(_.toSeq), groupIndeg)
    if (items.isEmpty || groups.isEmpty) return Array.empty
    val buckets = Array.fill(gm)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (item <- items) buckets(grp(item)) += item
    groups.flatMap(g => buckets(g))
  }
}
