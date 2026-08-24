// LeetCode 3096 - Minimum Levels to Gain More Points
// https://leetcode.com/problems/minimum-levels-to-gain-more-points/

object Solution {
  def minimumLevels(possible: Array[Int]): Int = {
    var s = 0
    possible.foreach(x => s += (if (x == 0) -1 else x))
    var t = 0
    var i = 0
    while (i + 1 < possible.length) {
      val x = if (possible(i) == 0) -1 else possible(i)
      t += x
      if (t > s - t) return i + 1
      i += 1
    }
    -1
  }
}
