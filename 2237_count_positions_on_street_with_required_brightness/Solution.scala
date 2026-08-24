// LeetCode 2237 - Count Positions on Street With Required Brightness
// https://leetcode.com/problems/count-positions-on-street-with-required-brightness/

object Solution {
  def meetRequirement(n: Int, lights: Array[Array[Int]], requirement: Array[Int]): Int = {
    val diff = new Array[Int](n + 1)
    for (light <- lights) {
      val pos = light(0)
      val r = light(1)
      val l = math.max(0, pos - r)
      val rr = math.min(n - 1, pos + r)
      diff(l) += 1
      diff(rr + 1) -= 1
    }
    var ans = 0
    var cur = 0
    var i = 0
    while (i < n) {
      cur += diff(i)
      if (cur >= requirement(i)) ans += 1
      i += 1
    }
    ans
  }
}
