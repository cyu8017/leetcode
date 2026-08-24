// LeetCode 3271 - Hash Divided String
// https://leetcode.com/problems/hash-divided-string/

object Solution {
  def stringHash(s: String, k: Int): String = {
    val outSb = new StringBuilder(s.length / k)
    var i = 0
    while (i < s.length) {
      var sum = 0
      var j = i
      while (j < i + k) {
        sum += s.charAt(j) - 'a'
        j += 1
      }
      outSb.append(('a' + sum % 26).toChar)
      i += k
    }
    outSb.toString
  }
}
