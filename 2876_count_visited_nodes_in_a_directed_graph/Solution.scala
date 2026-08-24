// LeetCode 2876 - Count Visited Nodes in a Directed Graph
// https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

object Solution {
  private var edges: Array[Int] = _
  private var ans: Array[Int] = _
  private var state: Array[Int] = _
  private var stack: scala.collection.mutable.ArrayBuffer[Int] = _

  def countVisitedNodes(edgesList: Array[Int]): Array[Int] = {
    val n = edgesList.length
    edges = edgesList
    ans = Array.fill(n)(0)
    state = Array.fill(n)(0)
    stack = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (i <- 0 until n if state(i) == 0) dfs(i)
    ans
  }

  private def dfs(u: Int): Unit = {
    state(u) = 1
    stack += u
    val v = edges(u)
    if (state(v) == 0) dfs(v)
    else if (state(v) == 1) {
      var idx = stack.length - 1
      while (stack(idx) != v) idx -= 1
      val cyc = stack.length - idx
      for (i <- idx until stack.length) ans(stack(i)) = cyc
    }
    if (ans(u) == 0) ans(u) = ans(edges(u)) + 1
    state(u) = 2
    stack.remove(stack.length - 1)
  }
}
