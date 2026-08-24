// LeetCode 2013 - Detect Squares
// https://leetcode.com/problems/detect-squares/

class DetectSquares() {
  private val cnt = scala.collection.mutable.Map.empty[Long, Int]

  private def key(x: Int, y: Int): Long = (x.toLong << 32) ^ (y.toLong & 0xffffffffL)

  def add(point: Array[Int]): Unit = {
    val k = key(point(0), point(1))
    cnt(k) = cnt.getOrElse(k, 0) + 1
  }

  def count(point: Array[Int]): Int = {
    val x = point(0)
    val y = point(1)
    var ans = 0
    cnt.foreach { case (k, c) =>
      val px = (k >> 32).toInt
      val py = k.toInt
      if (px != x && py != y && math.abs(px - x) == math.abs(py - y)) {
        val c1 = cnt.getOrElse(key(px, y), 0)
        val c2 = cnt.getOrElse(key(x, py), 0)
        ans += c * c1 * c2
      }
    }
    ans
  }
}
