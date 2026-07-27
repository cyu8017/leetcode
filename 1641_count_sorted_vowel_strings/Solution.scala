// LeetCode 1641 - Count Sorted Vowel Strings
// https://leetcode.com/problems/count-sorted-vowel-strings/

object Solution {
  def countVowelStrings(n: Int): Int = {
    def comb(nn: Int, rr: Int): Int = {
      var res = 1L
      val r = math.min(rr, nn - rr)
      var i = 0
      while (i < r) {
        res = res * (nn - i) / (i + 1)
        i += 1
      }
      res.toInt
    }
    comb(n + 4, 4)
  }
}
