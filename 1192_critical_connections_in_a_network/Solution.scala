// LeetCode 1192 - Critical Connections in a Network
// https://leetcode.com/problems/critical-connections-in-a-network/

object Solution {
  def criticalConnections(n: Int, connections: List[List[Int]]): List[List[Int]] = {
    val graph = Array.fill(n)(scala.collection.mutable.ListBuffer.empty[Int])
    for (e <- connections) {
      graph(e(0)) += e(1)
      graph(e(1)) += e(0)
    }
    val disc = Array.fill(n)(-1)
    val low = Array.fill(n)(-1)
    var time = 0
    val bridges = scala.collection.mutable.ListBuffer.empty[List[Int]]
    def dfs(node: Int, parent: Int): Unit = {
      disc(node) = time
      low(node) = time
      time += 1
      for (nxt <- graph(node) if nxt != parent) {
        if (disc(nxt) == -1) {
          dfs(nxt, node)
          low(node) = math.min(low(node), low(nxt))
          if (low(nxt) > disc(node)) bridges += List(math.min(node, nxt), math.max(node, nxt))
        } else low(node) = math.min(low(node), disc(nxt))
      }
    }
    dfs(0, -1)
    bridges.toList
  }
}
