// LeetCode 1697 - Checking Existence of Edge Length Limited Paths
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

object Solution {
  def distanceLimitedPathsExist(n: Int, edgeList: Array[Array[Int]], queries: Array[Array[Int]]): Array[Boolean] = {
    val parent = Array.tabulate(n)(identity)
    def find(x0: Int): Int = {
      var x = x0
      while (x != parent(x)) {
        parent(x) = parent(parent(x))
        x = parent(x)
      }
      x
    }
    val edges = edgeList.sortBy(_(2))
    val qs = queries.zipWithIndex.sortBy(_._1(2))
    val ans = Array.fill(queries.length)(false)
    var i = 0
    for ((q, idx) <- qs) {
      while (i < edges.length && edges(i)(2) < q(2)) {
        val a = edges(i)(0)
        val b = edges(i)(1)
        parent(find(a)) = find(b)
        i += 1
      }
      ans(idx) = find(q(0)) == find(q(1))
    }
    ans
  }
}
