// LeetCode 2156 - Find Substring With Given Hash Value
// https://leetcode.com/problems/find-substring-with-given-hash-value/

object Solution {
  def subStrHash(s: String, power: Int, modulo: Int, k: Int, hashValue: Int): String = {
    val n = s.length
    var pk = 1L
    var i = 0
    while (i < k - 1) {
      pk = pk * power % modulo
      i += 1
    }
    var h = 0L
    var ans = 0
    i = n - 1
    while (i >= n - k) {
      h = (h * power + (s.charAt(i) - 'a' + 1)) % modulo
      i -= 1
    }
    if (h == hashValue) ans = n - k
    i = n - k - 1
    while (i >= 0) {
      h = (h - (s.charAt(i + k) - 'a' + 1) * pk % modulo + modulo) % modulo
      h = (h * power + (s.charAt(i) - 'a' + 1)) % modulo
      if (h == hashValue) ans = i
      i -= 1
    }
    s.substring(ans, ans + k)
  }
}
