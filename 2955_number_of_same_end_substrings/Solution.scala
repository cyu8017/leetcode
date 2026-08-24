// LeetCode 2955 - Number of Same-End Substrings
// https://leetcode.com/problems/number-of-same-end-substrings/

object Solution {
  def sameEndSubstringCount(s: String, queries: Array[Array[Int]]): Array[Int] = {
    val n = s.length
    val pref = Array.ofDim[Array[Int]](n + 1)
    pref(0) = Array.ofDim[Int](26)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i).clone()
      pref(i + 1)(s.charAt(i) - 'a') += 1
      i += 1
    }
    val ans = Array.ofDim[Int](queries.length)
    var qi = 0
    while (qi < queries.length) {
      val l = queries(qi)(0)
      val r = queries(qi)(1)
      var total = 0
      var c = 0
      while (c < 26) {
        val cnt = pref(r + 1)(c) - pref(l)(c)
        total += cnt * (cnt + 1) / 2
        c += 1
      }
      ans(qi) = total
      qi += 1
    }
    ans
  }
}
