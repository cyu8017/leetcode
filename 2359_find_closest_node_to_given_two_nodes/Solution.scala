// LeetCode 2359 - Find Closest Node to Given Two Nodes
// https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

object Solution {
  def closestMeetingNode(edges: Array[Int], node1: Int, node2: Int): Int = {
    val n = edges.length

    def dist(start: Int): Array[Int] = {
      val d = Array.fill(n)(-1)
      var cur = start
      var step = 0
      while (cur != -1 && d(cur) == -1) {
        d(cur) = step
        cur = edges(cur)
        step += 1
      }
      d
    }

    val d1 = dist(node1)
    val d2 = dist(node2)
    var ans = -1
    var best = Int.MaxValue
    var i = 0
    while (i < n) {
      if (d1(i) != -1 && d2(i) != -1) {
        val mx = math.max(d1(i), d2(i))
        if (mx < best) {
          best = mx
          ans = i
        }
      }
      i += 1
    }
    ans
  }
}
