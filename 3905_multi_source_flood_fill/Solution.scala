// LeetCode 3905 - Multi Source Flood Fill
// https://leetcode.com/problems/multi-source-flood-fill/

object Solution {
  def colorGrid(n: Int, m: Int, sources: Array[Array[Int]]): Array[Array[Int]] = {
    val ans = Array.ofDim[Int](n, m)
    var q = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    sources.foreach { s => q += s }
    val dirs = Array(-1, 0, 1, 0, -1)
    q.foreach { s => ans(s(0))(s(1)) = s(2) }
    while (q.nonEmpty) {
      val vis = scala.collection.mutable.TreeMap.empty[Long, Int]
      q.foreach { curr =>
        val r = curr(0)
        val c = curr(1)
        val color = curr(2)
        var i = 0
        while (i < 4) {
          val x = r + dirs(i)
          val y = c + dirs(i + 1)
          if (x >= 0 && x < n && y >= 0 && y < m && ans(x)(y) == 0) {
            val key = (x.toLong << 32) | (y.toLong & 0xffffffffL)
            if (!vis.contains(key) || color > vis(key)) vis(key) = color
          }
          i += 1
        }
      }
      q.clear()
      vis.foreach { case (key, color) =>
        val x = (key >> 32).toInt
        val y = key.toInt
        ans(x)(y) = color
        q += Array(x, y, color)
      }
    }
    ans
  }
}
