// LeetCode 3039 - Apply Operations to Make String Empty
// https://leetcode.com/problems/apply-operations-to-make-string-empty/

object Solution {
  def lastNonEmptyString(s: String): String = {
    val cnt = Array.ofDim[Int](26)
    val last = Array.ofDim[Int](26)
    var mx = 0
    var i = 0
    while (i < s.length) {
      val c = s.charAt(i) - 'a'
      cnt(c) += 1
      last(c) = i
      mx = math.max(mx, cnt(c))
      i += 1
    }
    val ans = new StringBuilder
    i = 0
    while (i < s.length) {
      val c = s.charAt(i) - 'a'
      if (cnt(c) == mx && last(c) == i) ans.append(s.charAt(i))
      i += 1
    }
    ans.toString
  }
}
