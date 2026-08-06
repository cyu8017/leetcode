// LeetCode 1961 - Check If String Is a Prefix of Array
// https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

object Solution {
  def isPrefixString(s: String, words: Array[String]): Boolean = {
    val built = new StringBuilder
    for (w <- words) {
      built.append(w)
      val cur = built.toString
      if (cur == s) return true
      if (cur.length > s.length || !s.startsWith(cur)) return false
    }
    false
  }
}
