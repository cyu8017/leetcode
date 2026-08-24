// LeetCode 2001 - Number of Pairs of Interchangeable Rectangles
// https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

object Solution {
  def interchangeableRectangles(rectangles: Array[Array[Int]]): Long = {
    def gcd(a0: Int, b0: Int): Int = {
      var a = a0
      var b = b0
      while (b != 0) {
        val t = a % b
        a = b
        b = t
      }
      a
    }
    val freq = scala.collection.mutable.Map.empty[(Int, Int), Int]
    var ans = 0L
    rectangles.foreach { rect =>
      val g = gcd(rect(0), rect(1))
      val key = (rect(0) / g, rect(1) / g)
      val f = freq.getOrElse(key, 0)
      ans += f
      freq(key) = f + 1
    }
    ans
  }
}
