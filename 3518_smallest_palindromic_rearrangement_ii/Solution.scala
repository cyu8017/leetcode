// LeetCode 3518 - Smallest Palindromic Rearrangement II
// https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

object Solution {
  val MAX = 1000001

  def nCk(n0: Int, kk0: Int): Int = {
    if (kk0 < 0 || kk0 > n0) return 0
    var res = 1L
    var kk = kk0
    val n = n0
    if (kk > n - kk) kk = n - kk
    var i = 1
    while (i <= kk) {
      res = res * (n - i + 1) / i
      if (res >= MAX) return MAX
      i += 1
    }
    res.toInt
  }

  def countArr(h: Array[Int]): Int = {
    var total = 0
    for (f <- h) total += f
    var res = 1L
    for (f <- h) {
      res *= nCk(total, f)
      if (res >= MAX) return MAX
      total -= f
    }
    res.toInt
  }

  def smallestPalindrome(s: String, k0: Int): String = {
    val cnt = new Array[Int](26)
    for (c <- s.toCharArray) cnt(c - 'a') += 1
    var odd = 0
    for (c <- cnt) if (c % 2 != 0) odd += 1
    if (odd > 1) return ""
    val half = new Array[Int](26)
    var mid: Char = 0
    var i = 0
    while (i < 26) {
      half(i) = cnt(i) / 2
      if (cnt(i) % 2 != 0) mid = ('a' + i).toChar
      i += 1
    }
    var k = k0
    if (countArr(half) < k) return ""
    var halfLen = 0
    for (f <- half) halfLen += f
    val left = new StringBuilder
    var t = 0
    while (t < halfLen) {
      i = 0
      var placed = false
      while (i < 26 && !placed) {
        if (half(i) != 0) {
          half(i) -= 1
          val arr = countArr(half)
          if (arr >= k) {
            left.append(('a' + i).toChar)
            placed = true
          } else {
            k -= arr
            half(i) += 1
          }
        }
        if (!placed) i += 1
      }
      t += 1
    }
    val res = new StringBuilder
    res.append(left)
    if (mid != 0) res.append(mid)
    i = left.length - 1
    while (i >= 0) { res.append(left.charAt(i)); i -= 1 }
    res.toString
  }
}
