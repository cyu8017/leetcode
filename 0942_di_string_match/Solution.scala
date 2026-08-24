// LeetCode 0942 - DI String Match
// https://leetcode.com/problems/di-string-match/

object Solution {
  def diStringMatch(s: String): Array[Int] = {
    var lo = 0
    var hi = s.length
    val ans = Array.ofDim[Int](s.length + 1)
    var k = 0
    s.foreach { ch =>
      if (ch == 'I') { ans(k) = lo; lo += 1 }
      else { ans(k) = hi; hi -= 1 }
      k += 1
    }
    ans(k) = lo
    ans
  }
}
