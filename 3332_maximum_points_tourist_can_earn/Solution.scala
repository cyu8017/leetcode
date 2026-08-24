// LeetCode 3332 - Maximum Points Tourist Can Earn
// https://leetcode.com/problems/maximum-points-tourist-can-earn/

object Solution {
  def maxScore(n: Int, k: Int, stayScore: Array[Array[Int]], travelScore: Array[Array[Int]]): Int = {
    var dp = new Array[Int](n)
    var day = 0
    while (day < k) {
      val ndp = Array.fill(n)(-(1 << 30))
      var dest = 0
      while (dest < n) {
        var best = -(1 << 30)
        var src = 0
        while (src < n) {
          var v = dp(src)
          if (src == dest) v += stayScore(day)(dest)
          else v += travelScore(src)(dest)
          if (v > best) best = v
          src += 1
        }
        ndp(dest) = best
        dest += 1
      }
      dp = ndp
      day += 1
    }
    var ans = dp(0)
    var i = 1
    while (i < n) {
      if (dp(i) > ans) ans = dp(i)
      i += 1
    }
    ans
  }
}
