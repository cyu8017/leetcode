// LeetCode 3241 - Time Taken to Mark All Nodes
// https://leetcode.com/problems/time-taken-to-mark-all-nodes/

object Solution {
  class MarkNode(var node: Int = 0, var time: Int = 0)
  class Top2(var top1: MarkNode = new MarkNode(), var top2: MarkNode = new MarkNode())

  def timeTaken(edges: Array[Array[Int]]): Array[Int] = {
    val n = edges.length + 1
    val ans = new Array[Int](n)
    val tree = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    val dp = Array.fill(n)(new Top2())
    for (e <- edges) {
      tree(e(0)) += e(1)
      tree(e(1)) += e(0)
    }
    def getTime(u: Int): Int = if (u % 2 == 0) 2 else 1
    def dfs(u: Int, prev: Int): Int = {
      var t1 = new MarkNode()
      var t2 = new MarkNode()
      for (v <- tree(u) if v != prev) {
        val t = dfs(v, u) + getTime(v)
        if (t >= t1.time) {
          t2 = t1
          t1 = new MarkNode(v, t)
        } else if (t > t2.time) {
          t2 = new MarkNode(v, t)
        }
      }
      dp(u).top1 = t1
      dp(u).top2 = t2
      t1.time
    }
    def reroot(u: Int, prev: Int, maxTime: Int): Unit = {
      ans(u) = maxTime
      if (dp(u).top1.time > ans(u)) ans(u) = dp(u).top1.time
      for (v <- tree(u) if v != prev) {
        var side = dp(u).top1.time
        if (dp(u).top1.node == v) side = dp(u).top2.time
        val newMax = math.max(maxTime, side)
        reroot(v, u, getTime(u) + newMax)
      }
    }
    dfs(0, -1)
    reroot(0, -1, 0)
    ans
  }
}
