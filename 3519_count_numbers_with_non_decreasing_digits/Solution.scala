// LeetCode 3519 - Count Numbers with Non-Decreasing Digits
// https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

object Solution {
  val MOD = 1000000007

  def toDigits(s0: String, b: Int): java.util.ArrayList[Integer] = {
    var s = s0
    if (s == "0") {
      val z = new java.util.ArrayList[Integer]()
      z.add(0)
      return z
    }
    val digs = new java.util.ArrayList[Integer]()
    while (!(s.length == 1 && s.charAt(0) == '0')) {
      var rem = 0
      val q = new StringBuilder
      for (c <- s.toCharArray) {
        val cur = rem * 10 + (c - '0')
        val d = cur / b
        rem = cur % b
        if (q.length > 0 || d != 0) q.append(('0' + d).toChar)
      }
      digs.add(rem)
      s = if (q.length == 0) "0" else q.toString
    }
    java.util.Collections.reverse(digs)
    digs
  }

  def dec(s: String): String = {
    val a = s.toCharArray
    var i = a.length - 1
    while (i >= 0 && a(i) == '0') { a(i) = '9'; i -= 1 }
    if (i < 0) return "0"
    a(i) = (a(i) - 1).toChar
    val t = new String(a)
    var p = 0
    while (p + 1 < t.length && t.charAt(p) == '0') p += 1
    t.substring(p)
  }

  def dfs(pos: Int, last: Int, tight: Boolean, digs: java.util.List[Integer], b: Int, m: Int, memo: scala.collection.mutable.HashMap[String, Int]): Int = {
    if (pos == m) return 1
    val key = pos + "," + last + "," + (if (tight) 1 else 0)
    if (memo.contains(key)) return memo(key)
    val up = if (tight) digs.get(pos).intValue() else b - 1
    var res = 0
    var d = last
    while (d <= up) {
      res = (res + dfs(pos + 1, d, tight && d == up, digs, b, m, memo)) % MOD
      d += 1
    }
    memo(key) = res
    res
  }

  def countUpto(digs: java.util.List[Integer], b: Int): Int = {
    val m = digs.size()
    val memo = scala.collection.mutable.HashMap.empty[String, Int]
    dfs(0, 0, true, digs, b, m, memo)
  }

  def countNumbers(l: String, r: String, b: Int): Int = {
    val rd = toDigits(r, b)
    val ld = toDigits(dec(l), b)
    (countUpto(rd, b) - countUpto(ld, b) + MOD) % MOD
  }
}
