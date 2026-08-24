// LeetCode 2360 - Longest Cycle in a Graph
// https://leetcode.com/problems/longest-cycle-in-a-graph/

object Solution {
  def longestCycle(edges: Array[Int]): Int = {
    val n = edges.length
    val vis = Array.fill(n)(false)
    var ans = -1
    var i = 0
    while (i < n) {
      if (!vis(i)) {
        val dist = scala.collection.mutable.Map.empty[Int, Int]
        var cur = i
        var step = 0
        while (cur != -1 && !vis(cur)) {
          vis(cur) = true
          dist(cur) = step
          cur = edges(cur)
          step += 1
        }
        if (cur != -1 && dist.contains(cur)) {
          ans = math.max(ans, step - dist(cur))
        }
      }
      i += 1
    }
    ans
  }
}
