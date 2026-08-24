// LeetCode 3233 - Find the Count of Numbers Which Are Not Special
// https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

object Solution {
  val M = 31623
  lazy val primes: Array[Boolean] = {
    val p = Array.fill(M + 1)(true)
    p(0) = false
    p(1) = false
    var i = 2
    while (i <= M) {
      if (p(i)) {
        var j = i * 2
        while (j <= M) { p(j) = false; j += i }
      }
      i += 1
    }
    p
  }

  def nonSpecialCount(l: Int, r: Int): Int = {
    val lo = math.ceil(math.sqrt(l.toDouble)).toInt
    val hi = math.floor(math.sqrt(r.toDouble)).toInt
    var cnt = 0
    var i = lo
    while (i <= hi) {
      if (primes(i)) cnt += 1
      i += 1
    }
    r - l + 1 - cnt
  }
}
