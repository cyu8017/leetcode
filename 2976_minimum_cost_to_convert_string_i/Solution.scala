// LeetCode 2976 - Minimum Cost to Convert String I
// https://leetcode.com/problems/minimum-cost-to-convert-string-i/

object Solution {
  def minimumCost(source: String, target: String, original: Array[String], changed: Array[String], cost: Array[Int]): Long = {
    val inf = 1L << 60
    val dist = Array.fill(26, 26)(inf)
    var i = 0
    while (i < 26) { dist(i)(i) = 0; i += 1 }
    i = 0
    while (i < original.length) {
      val u = original(i).charAt(0) - 'a'
      val v = changed(i).charAt(0) - 'a'
      val ww = cost(i).toLong
      if (ww < dist(u)(v)) dist(u)(v) = ww
      i += 1
    }
    var k = 0
    while (k < 26) {
      i = 0
      while (i < 26) {
        var j = 0
        while (j < 26) {
          if (dist(i)(k) + dist(k)(j) < dist(i)(j)) dist(i)(j) = dist(i)(k) + dist(k)(j)
          j += 1
        }
        i += 1
      }
      k += 1
    }
    var ans = 0L
    i = 0
    while (i < source.length) {
      val a = source.charAt(i) - 'a'
      val b = target.charAt(i) - 'a'
      if (dist(a)(b) >= inf / 2) return -1
      ans += dist(a)(b)
      i += 1
    }
    ans
  }
}
