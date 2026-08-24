// LeetCode 2768 - Number of Black Blocks
// https://leetcode.com/problems/number-of-black-blocks/

object Solution {
  def countBlackBlocks(m: Int, n: Int, coordinates: Array[Array[Int]]): Array[Long] = {
    val cnt = scala.collection.mutable.Map.empty[Long, Int]
    coordinates.foreach { c =>
      val x = c(0)
      val y = c(1)
      var i = x - 1
      while (i <= x) {
        var j = y - 1
        while (j <= y) {
          if (i >= 0 && j >= 0 && i < m - 1 && j < n - 1) {
            val key = (i.toLong << 32) | (j.toLong & 0xffffffffL)
            cnt(key) = cnt.getOrElse(key, 0) + 1
          }
          j += 1
        }
        i += 1
      }
    }
    val ans = Array.ofDim[Long](5)
    ans(0) = (m.toLong - 1) * (n.toLong - 1)
    cnt.values.foreach { v =>
      ans(v) += 1
      ans(0) -= 1
    }
    ans
  }
}
