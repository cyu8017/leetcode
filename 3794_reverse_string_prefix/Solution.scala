// LeetCode 3794 - Reverse String Prefix
// https://leetcode.com/problems/reverse-string-prefix/

object Solution {
  def reversePrefix(s: String, k: Int): String = {
    val arr = s.toCharArray
    reverse(arr, 0, 0 + k)
    new String(arr)
  }

  private def reverse(a: Array[Char], l: Int, r: Int): Unit = {
    var i = l
    var j = r - 1
    while (i < j) {
      val t = a(i); a(i) = a(j); a(j) = t
      i += 1
      j -= 1
    }
  }
}
