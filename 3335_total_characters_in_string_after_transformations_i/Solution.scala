// LeetCode 3335 - Total Characters in String After Transformations I
// https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

object Solution {
  def lengthAfterTransformations(s: String, t: Int): Int = {
    val mod = 1000000007
    var cnt = new Array[Int](26)
    for (c <- s) cnt(c - 'a') += 1
    var step = 0
    while (step < t) {
      val ncnt = new Array[Int](26)
      var i = 0
      while (i < 25) {
        ncnt(i + 1) = (ncnt(i + 1) + cnt(i)) % mod
        i += 1
      }
      ncnt(0) = (ncnt(0) + cnt(25)) % mod
      ncnt(1) = (ncnt(1) + cnt(25)) % mod
      cnt = ncnt
      step += 1
    }
    var ans = 0
    for (v <- cnt) ans = (ans + v) % mod
    ans
  }
}
