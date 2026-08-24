// LeetCode 2645 - Minimum Additions to Make Valid String
// https://leetcode.com/problems/minimum-additions-to-make-valid-string/

object Solution {
  def addMinimum(word: String): Int = {
    var ans = 0
    var expect = 0
    var i = 0
    val n = word.length
    while (i < n) {
      val need = ('a' + expect).toChar
      if (word.charAt(i) == need) i += 1
      else ans += 1
      expect = (expect + 1) % 3
    }
    ans += (3 - expect) % 3
    ans
  }
}
