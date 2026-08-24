// LeetCode 0864 - Shortest Path to Get All Keys
// https://leetcode.com/problems/shortest-path-to-get-all-keys/

object Solution {
  def shortestPathAllKeys(grid: Array[String]): Int = {
    val m = grid.length
    val n = grid(0).length
    var allKeys = 0
    var sr = 0
    var sc = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        val ch = grid(i).charAt(j)
        if (ch == '@') { sr = i; sc = j }
        else if (ch >= 'a' && ch <= 'f') allKeys |= 1 << (ch - 'a')
        j += 1
      }
      i += 1
    }
    def encode(r: Int, c: Int, mask: Int): Long = (r.toLong << 20) | (c.toLong << 10) | mask
    val queue = scala.collection.mutable.Queue((sr, sc, 0, 0))
    val seen = scala.collection.mutable.Set(encode(sr, sc, 0))
    val dr = Array(1, -1, 0, 0)
    val dc = Array(0, 0, 1, -1)
    while (queue.nonEmpty) {
      val (r, c, mask, dist) = queue.dequeue()
      if (mask == allKeys) return dist
      var k = 0
      while (k < 4) {
        val nr = r + dr(k)
        val nc = c + dc(k)
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid(nr).charAt(nc) != '#') {
          val cell = grid(nr).charAt(nc)
          var nmask = mask
          if (cell >= 'a' && cell <= 'f') nmask |= 1 << (cell - 'a')
          if (!(cell >= 'A' && cell <= 'F' && (mask & (1 << (cell - 'A'))) == 0)) {
            if (seen.add(encode(nr, nc, nmask))) queue.enqueue((nr, nc, nmask, dist + 1))
          }
        }
        k += 1
      }
    }
    -1
  }
}
