// LeetCode 3964 - Minimum Lights to Illuminate a Road
// https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/

object Solution {
  def minLights(lights: Array[Int]): Int = {
    val n = lights.length
    val d = new Array[Int](n)
    var i = 0
    while (i < n) {
      val v = lights(i)
      if (v > 0) {
        val l = math.max(0, i - v)
        val r = math.min(n - 1, i + v)
        d(l) += 1
        if (r + 1 < n) d(r + 1) -= 1
      }
      i += 1
    }
    var s = 0
    var cnt = 0
    var ans = 0
    for (x <- d) {
      s += x
      if (s == 0) cnt += 1
      else {
        ans += (cnt + 2) / 3
        cnt = 0
      }
    }
    ans += (cnt + 2) / 3
    ans
  }
}
