// LeetCode 3333 - Find the Original Typed String II
// https://leetcode.com/problems/find-the-original-typed-string-ii/

object Solution {
  def possibleStringCount(word: String, k: Int): Int = {
    val mod = 1000000007
    val groups = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < word.length) {
      var j = i
      while (j < word.length && word.charAt(j) == word.charAt(i)) j += 1
      groups += j - i
      i = j
    }
    var total = 1
    for (g <- groups) total = (total.toLong * g % mod).toInt
    if (k <= groups.length) return total
    val need = k - 1
    var dp = new Array[Int](need)
    dp(0) = 1
    for (g <- groups) {
      val ndp = new Array[Int](need)
      val pref = new Array[Int](need + 1)
      i = 0
      while (i < need) {
        pref(i + 1) = (pref(i) + dp(i)) % mod
        i += 1
      }
      var s = 0
      while (s < need) {
        var lo = s - g
        if (lo < 0) lo = 0
        val hi = s - 1
        if (hi >= 0) ndp(s) = (pref(hi + 1) - pref(lo) + mod) % mod
        s += 1
      }
      dp = ndp
    }
    var bad = 0
    for (v <- dp) bad = (bad + v) % mod
    (total - bad + mod) % mod
  }
}
