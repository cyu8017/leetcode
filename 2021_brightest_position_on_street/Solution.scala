// LeetCode 2021 - Brightest Position on Street
// https://leetcode.com/problems/brightest-position-on-street/

object Solution {
  def brightestPosition(lights: Array[Array[Int]]): Int = {
    val events = scala.collection.mutable.ArrayBuffer.empty[(Int, Int)]
    lights.foreach { light =>
      val pos = light(0)
      val r = light(1)
      events += ((pos - r, 1))
      events += ((pos + r + 1, -1))
    }
    val sorted = events.sortBy(e => (e._1, -e._2))
    var best = 0
    var cur = 0
    var ans = 0
    sorted.foreach { case (x, d) =>
      cur += d
      if (cur > best) { best = cur; ans = x }
    }
    ans
  }
}
