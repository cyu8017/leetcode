// LeetCode 0848 - Shifting Letters
// https://leetcode.com/problems/shifting-letters/

object Solution {
  def shiftingLetters(s: String, shifts: Array[Int]): String = {
    val arr = s.toCharArray
    var total = 0
    var i = arr.length - 1
    while (i >= 0) {
      total = (total + shifts(i)) % 26
      arr(i) = ((arr(i) - 'a' + total) % 26 + 'a').toChar
      i -= 1
    }
    new String(arr)
  }
}
