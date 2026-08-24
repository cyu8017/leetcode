// LeetCode 0803 - Bricks Falling When Hit
// https://leetcode.com/problems/bricks-falling-when-hit/

object Solution {
  def hitBricks(grid: Array[Array[Int]], hits: Array[Array[Int]]): Array[Int] = {
    val m = grid.length
    val n = grid(0).length
    val roof = m * n
    val parent = Array.tabulate(roof + 1)(identity)
    val size = Array.fill(roof + 1)(1)
    def find(x0: Int): Int = {
      var x = x0
      while (parent(x) != x) {
        parent(x) = parent(parent(x))
        x = parent(x)
      }
      x
    }
    def unite(a: Int, b: Int): Unit = {
      val ra = find(a)
      val rb = find(b)
      if (ra == rb) return
      parent(ra) = rb
      size(rb) += size(ra)
    }
    def idx(r: Int, c: Int): Int = r * n + c
    val status = grid.map(_.clone())
    hits.foreach { h => status(h(0))(h(1)) = 0 }
    val dr = Array(-1, 1, 0, 0)
    val dc = Array(0, 0, -1, 1)
    var r = 0
    while (r < m) {
      var c = 0
      while (c < n) {
        if (status(r)(c) != 0) {
          if (r == 0) unite(idx(r, c), roof)
          var k = 0
          while (k < 4) {
            val nr = r + dr(k)
            val nc = c + dc(k)
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && status(nr)(nc) == 1) {
              unite(idx(r, c), idx(nr, nc))
            }
            k += 1
          }
        }
        c += 1
      }
      r += 1
    }
    val answer = Array.ofDim[Int](hits.length)
    var i = hits.length - 1
    while (i >= 0) {
      r = hits(i)(0)
      val c = hits(i)(1)
      if (grid(r)(c) != 0) {
        val prev = size(find(roof))
        status(r)(c) = 1
        if (r == 0) unite(idx(r, c), roof)
        var k = 0
        while (k < 4) {
          val nr = r + dr(k)
          val nc = c + dc(k)
          if (nr >= 0 && nr < m && nc >= 0 && nc < n && status(nr)(nc) == 1) {
            unite(idx(r, c), idx(nr, nc))
          }
          k += 1
        }
        val curr = size(find(roof))
        answer(i) = math.max(0, curr - prev - 1)
      }
      i -= 1
    }
    answer
  }
}
