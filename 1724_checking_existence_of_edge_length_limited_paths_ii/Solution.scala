// LeetCode 1724 - Checking Existence of Edge Length Limited Paths II
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/

class DistanceLimitedPathsExist(n: Int, edgeList: Array[Array[Int]]) {
  private val weights = scala.collection.mutable.ArrayBuffer.empty[Int]
  private val versions = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]

  {
    val edges = edgeList
      .map(edge => (edge(2), edge(0), edge(1)))
      .sorted
    val parent = Array.tabulate(n)(identity)
    val size = Array.fill(n)(1)
    def find(start: Int): Int = {
      var x = start
      while (parent(x) != x) {
        parent(x) = parent(parent(x))
        x = parent(x)
      }
      x
    }
    var i = 0
    while (i < edges.length) {
      val weight = edges(i)._1
      while (i < edges.length && edges(i)._1 == weight) {
        var ra = find(edges(i)._2)
        var rb = find(edges(i)._3)
        if (ra != rb) {
          if (size(ra) < size(rb)) {
            val tmp = ra
            ra = rb
            rb = tmp
          }
          parent(rb) = ra
          size(ra) += size(rb)
        }
        i += 1
      }
      weights += weight
      versions += parent.clone()
    }
  }

  def query(p: Int, q: Int, limit: Int): Boolean = {
    var lo = 0
    var hi = weights.length
    while (lo < hi) {
      val mid = (lo + hi) >>> 1
      if (weights(mid) < limit) lo = mid + 1 else hi = mid
    }
    val idx = lo - 1
    if (idx < 0) return p == q
    val parent = versions(idx)
    var rp = p
    while (parent(rp) != rp) rp = parent(rp)
    var rq = q
    while (parent(rq) != rq) rq = parent(rq)
    rp == rq
  }
}
