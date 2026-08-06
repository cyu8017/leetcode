// LeetCode 1319 - Number of Operations to Make Network Connected
// https://leetcode.com/problems/number-of-operations-to-make-network-connected/

object Solution {
  def makeConnected(n: Int, connections: Array[Array[Int]]): Int = {
    if (connections.length < n - 1) return -1
    val parent = Array.tabulate(n)(identity)
    def find(x: Int): Int = {
      var cur = x
      while (cur != parent(cur)) {
        parent(cur) = parent(parent(cur))
        cur = parent(cur)
      }
      cur
    }
    for (edge <- connections) {
      val ra = find(edge(0))
      val rb = find(edge(1))
      if (ra != rb) parent(ra) = rb
    }
    (0 until n).map(find).toSet.size - 1
  }
}
