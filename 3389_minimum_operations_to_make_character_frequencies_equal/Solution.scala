// LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
// https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/

object Solution {
  def makeStringGood(s: String): Int = {
    val freq = new Array[Int](26)
    for (c <- s) freq(c - 'a') += 1
    var ans = s.length
    var t = 1
    while (t <= s.length) {
      var pool = 0
      var i = 0
      while (i < 26) {
        if (freq(i) > t) pool += freq(i) - t
        i += 1
      }
      var deficit = 0
      i = 0
      while (i < 26) {
        if (freq(i) < t) deficit += t - freq(i)
        i += 1
      }
      val ops = math.max(pool, deficit)
      if (ops < ans) ans = ops
      t += 1
    }
    if (s.length < ans) ans = s.length
    ans
  }
}
