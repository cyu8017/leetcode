// LeetCode 0686 - Repeated String Match
// https://leetcode.com/problems/repeated-string-match/

object Solution {
  def repeatedStringMatch(a: String, b: String): Int = {
    val repeats = (b.length + a.length - 1) / a.length
    val built = new StringBuilder(a.length * (repeats + 1))
    var i = 0
    while (i < repeats) {
      built.append(a)
      i += 1
    }
    if (built.toString.contains(b)) return repeats
    built.append(a)
    if (built.toString.contains(b)) repeats + 1 else -1
  }
}
