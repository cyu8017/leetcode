// LeetCode 1719 - Number Of Ways To Reconstruct A Tree
// https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

object Solution {
  def checkWays(pairs: Array[Array[Int]]): Int = {
    val graph = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.Set[Int]]
    pairs.foreach { pair =>
      val a = pair(0)
      val b = pair(1)
      graph.getOrElseUpdate(a, scala.collection.mutable.Set.empty[Int]).add(b)
      graph.getOrElseUpdate(b, scala.collection.mutable.Set.empty[Int]).add(a)
    }
    val n = graph.size
    val root = graph.collectFirst { case (node, neighbors) if neighbors.size == n - 1 => node }
    if (root.isEmpty) {
      return 0
    }
    var ans = 1
    for ((node, neighbors) <- graph if node != root.get) {
      var parent = -1
      var parentDegree = n + 1
      neighbors.foreach { nei =>
        val neiDegree = graph(nei).size
        if (neiDegree >= neighbors.size && neiDegree < parentDegree) {
          parent = nei
          parentDegree = neiDegree
        }
      }
      if (parent == -1) {
        return 0
      }
      for (nei <- neighbors) {
        if (nei != parent && !graph(parent).contains(nei)) {
          return 0
        }
      }
      if (graph(parent).size == neighbors.size) {
        ans = 2
      }
    }
    ans
  }
}
