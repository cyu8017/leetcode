// LeetCode 2514 - Count Anagrams
// https://leetcode.com/problems/count-anagrams/

object Solution {
  def countAnagrams(s: String): Int = {
    val MOD = 1000000007
    def modPow(a0: Long, e0: Long): Long = {
      var res = 1L
      var a = a0 % MOD
      var e = e0
      while (e > 0) {
        if ((e & 1) != 0) res = res * a % MOD
        a = a * a % MOD
        e >>= 1
      }
      res
    }
    val trimmed = s.trim
    val words = if (trimmed.isEmpty) Array.empty[String] else trimmed.split("\\s+")
    var maxN = 0
    words.foreach { w => if (w.length > maxN) maxN = w.length }
    val fact = new Array[Long](maxN + 1)
    val invFact = new Array[Long](maxN + 1)
    fact(0) = 1
    var i = 1
    while (i <= maxN) {
      fact(i) = fact(i - 1) * i % MOD
      i += 1
    }
    if (maxN >= 0) invFact(maxN) = modPow(fact(maxN), MOD - 2)
    i = maxN
    while (i > 0) {
      invFact(i - 1) = invFact(i) * i % MOD
      i -= 1
    }
    var ans = 1L
    words.foreach { word =>
      val cnt = new Array[Int](26)
      var j = 0
      while (j < word.length) {
        cnt(word.charAt(j) - 'a') += 1
        j += 1
      }
      var cur = fact(word.length)
      j = 0
      while (j < 26) {
        cur = cur * invFact(cnt(j)) % MOD
        j += 1
      }
      ans = ans * cur % MOD
    }
    ans.toInt
  }
}
