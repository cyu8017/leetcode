// LeetCode 3889 - Mirror Frequency Distance
// https://leetcode.com/problems/mirror-frequency-distance/

object Solution {
  def mirrorFrequency(s: String): Int = {
    val freq = scala.collection.mutable.Map.empty[Char, Int]
    s.foreach { c => freq(c) = freq.getOrElse(c, 0) + 1 }
    var ans = 0
    val vis = scala.collection.mutable.Map.empty[Char, Boolean]
    freq.foreach { case (c, v) =>
      val m = if (c >= 'a' && c <= 'z') ('a' + 25 - (c - 'a')).toChar
              else ('0' + (9 - (c - '0'))).toChar
      if (!vis.getOrElse(m, false)) {
        vis(c) = true
        val mv = freq.getOrElse(m, 0)
        ans += math.abs(v - mv)
      }
    }
    ans
  }
}
