// LeetCode 3992 - Rearrange String to Avoid Character Pair
// https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/

object Solution {
  def rearrangeString(s: String, x: Char, y: Char): String = {
    val arr = s.toCharArray
    var i = 0
    var j = 0
    while (j < arr.length) {
      if (arr(j) == y) {
        val tmp = arr(i)
        arr(i) = arr(j)
        arr(j) = tmp
        i += 1
      }
      j += 1
    }
    new String(arr)
  }
}
