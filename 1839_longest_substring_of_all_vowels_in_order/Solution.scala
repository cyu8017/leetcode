// LeetCode 1839 - Longest Substring Of All Vowels in Order
// https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

object Solution {
  def longestBeautifulSubstring(word: String): Int = {
    val vowels = "aeiou"
    var best = 0
    for (start <- word.indices if word(start) == 'a') {
      val counts = Array.fill(5)(0)
      var end = start
      var cont = true
      while (end < word.length && cont) {
        val current = word(end)
        if (end > start && current < word(end - 1)) cont = false
        else {
          val idx = vowels.indexOf(current)
          if (idx < 0) cont = false
          else {
            counts(idx) += 1
            if (idx > 0 && counts(idx - 1) == 0) cont = false
            else if (counts.forall(_ > 0)) best = math.max(best, end - start + 1)
          }
        }
        if (cont) end += 1
      }
    }
    best
  }
}
