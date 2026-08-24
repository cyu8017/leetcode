// LeetCode 3138 - Minimum Length of Anagram Concatenation
// https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

object Solution {
  def minAnagramLength(s: String): Int = {
    val n = s.length
    val cnt = new Array[Int](26)
    var i = 0
    while (i < n) {
      cnt(s.charAt(i) - 'a') += 1
      i += 1
    }
    i = 1
    while (true) {
      if (n % i == 0 && check(s, n, cnt, i)) return i
      i += 1
    }
    n
  }

  private def check(s: String, n: Int, cnt: Array[Int], k: Int): Boolean = {
    var i = 0
    while (i < n) {
      val cnt1 = new Array[Int](26)
      var j = i
      while (j < i + k) {
        cnt1(s.charAt(j) - 'a') += 1
        j += 1
      }
      j = 0
      while (j < 26) {
        if (cnt1(j) * (n / k) != cnt(j)) return false
        j += 1
      }
      i += k
    }
    true
  }
}
