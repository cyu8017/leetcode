// LeetCode 2301 - Match Substring After Replacement
// https://leetcode.com/problems/match-substring-after-replacement/

object Solution {
  def matchReplacement(s: String, sub: String, mappings: Array[Array[Char]]): Boolean = {
    val allow = scala.collection.mutable.HashSet.empty[Int]
    for (m <- mappings) allow += ((m(0).toInt << 8) | m(1).toInt)
    val n = s.length
    val mlen = sub.length
    var i = 0
    while (i + mlen <= n) {
      var ok = true
      var j = 0
      while (j < mlen && ok) {
        val a = s.charAt(i + j)
        val b = sub.charAt(j)
        if (a != b && !allow.contains((b.toInt << 8) | a.toInt)) ok = false
        j += 1
      }
      if (ok) return true
      i += 1
    }
    false
  }
}
