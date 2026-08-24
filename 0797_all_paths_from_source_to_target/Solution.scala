// LeetCode 0797 - All Paths From Source to Target
// https://leetcode.com/problems/all-paths-from-source-to-target/

object Solution {
  def allPathsSourceTarget(graph: Array[Array[Int]]): List[List[Int]] = {
    val target = graph.length - 1
    val answer = scala.collection.mutable.ListBuffer.empty[List[Int]]
    val path = scala.collection.mutable.ListBuffer(0)
    def dfs(node: Int): Unit = {
      if (node == target) {
        answer += path.toList
        return
      }
      graph(node).foreach { nei =>
        path += nei
        dfs(nei)
        path.remove(path.length - 1)
      }
    }
    dfs(0)
    answer.toList
  }
}
