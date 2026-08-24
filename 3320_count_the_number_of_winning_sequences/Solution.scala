// LeetCode 3320 - Count the Number of Winning Sequences
// https://leetcode.com/problems/count-the-number-of-winning-sequences/

object Solution {
  def countWinningSequences(s: String): Int = {
    val mod = 1000000007
    val n = s.length
    val mp = new Array[Int](256)
    mp('F') = 0; mp('W') = 1; mp('E') = 2
    val beat = Array(2, 0, 1)
    val score = Array.ofDim[Int](3, 3)
    var a = 0
    while (a < 3) {
      var b = 0
      while (b < 3) {
        if (a == b) score(a)(b) = 0
        else if (beat(a) == b) score(a)(b) = 1
        else score(a)(b) = -1
        b += 1
      }
      a += 1
    }
    val offset = n
    var dp = Array.fill(3, 2 * n + 1)(0)
    val b0 = mp(s.charAt(0))
    a = 0
    while (a < 3) {
      dp(a)(score(a)(b0) + offset) = 1
      a += 1
    }
    var i = 1
    while (i < n) {
      val ndp = Array.fill(3, 2 * n + 1)(0)
      val b = mp(s.charAt(i))
      var last = 0
      while (last < 3) {
        var d = 0
        while (d <= 2 * n) {
          if (dp(last)(d) != 0) {
            a = 0
            while (a < 3) {
              if (a != last) {
                val nd = d + score(a)(b)
                if (nd >= 0 && nd <= 2 * n) {
                  ndp(a)(nd) = (ndp(a)(nd) + dp(last)(d)) % mod
                }
              }
              a += 1
            }
          }
          d += 1
        }
        last += 1
      }
      dp = ndp
      i += 1
    }
    var ans = 0
    a = 0
    while (a < 3) {
      var d = offset + 1
      while (d <= 2 * n) {
        ans = (ans + dp(a)(d)) % mod
        d += 1
      }
      a += 1
    }
    ans
  }
}
