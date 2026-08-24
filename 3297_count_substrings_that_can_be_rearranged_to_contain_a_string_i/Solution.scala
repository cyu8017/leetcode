// LeetCode 3297 - Count Substrings That Can Be Rearranged to Contain a String I
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

object Solution {
  def validSubstringCount(word1: String, word2: String): Long = {
    val need = new Array[Int](26)
    var required = 0
    for (c <- word2) {
      if (need(c - 'a') == 0) required += 1
      need(c - 'a') += 1
    }
    val have = new Array[Int](26)
    var formed = 0
    var ans = 0L
    var l = 0
    var r = 0
    while (r < word1.length) {
      val c = word1.charAt(r) - 'a'
      have(c) += 1
      if (have(c) == need(c) && need(c) > 0) formed += 1
      while (formed == required && l <= r) {
        ans += word1.length - r
        val c2 = word1.charAt(l) - 'a'
        if (have(c2) == need(c2) && need(c2) > 0) formed -= 1
        have(c2) -= 1
        l += 1
      }
      r += 1
    }
    ans
  }
}
