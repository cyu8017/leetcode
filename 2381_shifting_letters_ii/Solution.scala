// LeetCode 2381 - Shifting Letters II
// https://leetcode.com/problems/shifting-letters-ii/

object Solution {
  def shiftingLetters(s: String, shifts: Array[Array[Int]]): String = {
    val n = s.length
    val diff = Array.fill(n + 1)(0)
    shifts.foreach { sh =>
      val d = if (sh(2) == 0) -1 else 1
      diff(sh(0)) += d
      diff(sh(1) + 1) -= d
    }
    val arr = s.toCharArray
    var cur = 0
    var i = 0
    while (i < n) {
      cur = (cur + diff(i)) % 26
      if (cur < 0) cur += 26
      arr(i) = ('a' + (arr(i) - 'a' + cur) % 26).toChar
      i += 1
    }
    new String(arr)
  }
}
