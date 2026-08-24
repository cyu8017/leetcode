// LeetCode 2516 - Take K of Each Character From Left and Right
// https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

object Solution {
  def takeCharacters(s: String, k: Int): Int = {
    val n = s.length
    val cnt = new Array[Int](3)
    var i = 0
    while (i < n) {
      cnt(s.charAt(i) - 'a') += 1
      i += 1
    }
    if (cnt(0) < k || cnt(1) < k || cnt(2) < k) return -1
    val need = Array(cnt(0) - k, cnt(1) - k, cnt(2) - k)
    val window = new Array[Int](3)
    var left = 0
    var maxMid = 0
    var right = 0
    while (right < n) {
      window(s.charAt(right) - 'a') += 1
      while (window(0) > need(0) || window(1) > need(1) || window(2) > need(2)) {
        window(s.charAt(left) - 'a') -= 1
        left += 1
      }
      if (right - left + 1 > maxMid) maxMid = right - left + 1
      right += 1
    }
    n - maxMid
  }
}
