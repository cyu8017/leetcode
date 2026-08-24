// LeetCode 2249 - Count Lattice Points Inside a Circle
// https://leetcode.com/problems/count-lattice-points-inside-a-circle/

object Solution {
  def countLatticePoints(circles: Array[Array[Int]]): Int = {
    val seen = scala.collection.mutable.HashSet.empty[Long]
    for (c <- circles) {
      val x = c(0)
      val y = c(1)
      val r = c(2)
      var i = x - r
      while (i <= x + r) {
        var j = y - r
        while (j <= y + r) {
          if ((i - x) * (i - x) + (j - y) * (j - y) <= r * r)
            seen += ((i.toLong << 32) | (j.toLong & 0xffffffffL))
          j += 1
        }
        i += 1
      }
    }
    seen.size
  }
}
