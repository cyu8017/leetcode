// LeetCode 3932 - Count K-th Roots in a Range
// https://leetcode.com/problems/count-k-th-roots-in-a-range/

object Solution {
  def countKthRoots(l: Int, r: Int, k: Int): Int = {
    if (k == 1) return r - l + 1
    var ans = 0
    var x = 0L
    var done = false
    while (!done) {
      var y = 1L
      var tooBig = false
      var i = 0
      while (i < k && !tooBig && y <= r) {
        if (x != 0 && y > r.toLong / x) tooBig = true
        else y *= x
        i += 1
      }
      if (tooBig || y > r) done = true
      else {
        if (l <= y && y <= r) ans += 1
        x += 1
      }
    }
    ans
  }
}
