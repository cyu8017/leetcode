// LeetCode 2000 - Reverse Prefix of Word
// https://leetcode.com/problems/reverse-prefix-of-word/

object Solution {
  def reversePrefix(word: String, ch: Char): String = {
    val pos = word.indexOf(ch)
    if (pos < 0) word
    else {
      val arr = word.toCharArray
      var l = 0
      var r = pos
      while (l < r) {
        val tmp = arr(l)
        arr(l) = arr(r)
        arr(r) = tmp
        l += 1
        r -= 1
      }
      new String(arr)
    }
  }
}
