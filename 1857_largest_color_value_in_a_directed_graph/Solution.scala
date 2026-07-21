// LeetCode 1857 - Largest Color Value in a Directed Graph
// https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

import scala.collection.mutable

object Solution {
  def largestPathValue(colors: String, edges: Array[Array[Int]]): Int = {
    val n = colors.length
    val indegree = Array.fill(n)(0)
    val adjacency = Array.fill(n)(mutable.ArrayBuffer.empty[Int])
    for (edge <- edges) {
      adjacency(edge(0)) += edge(1)
      indegree(edge(1)) += 1
    }

    val queue = mutable.Queue[Int]()
    for (node <- 0 until n if indegree(node) == 0) {
      queue.enqueue(node)
    }

    val dp = Array.fill(n, 26)(0)
    for (node <- 0 until n) {
      dp(node)(colors(node) - 'a') = 1
    }

    var processed = 0
    var answer = 0
    while (queue.nonEmpty) {
      val node = queue.dequeue()
      processed += 1
      answer = math.max(answer, dp(node).max)
      for (neighbor <- adjacency(node)) {
        val neighborColor = colors(neighbor) - 'a'
        for (colorIndex <- 0 until 26) {
          var candidate = dp(node)(colorIndex)
          if (colorIndex == neighborColor) candidate += 1
          if (candidate > dp(neighbor)(colorIndex)) {
            dp(neighbor)(colorIndex) = candidate
          }
        }
        indegree(neighbor) -= 1
        if (indegree(neighbor) == 0) queue.enqueue(neighbor)
      }
    }
    if (processed == n) answer else -1
  }
}
