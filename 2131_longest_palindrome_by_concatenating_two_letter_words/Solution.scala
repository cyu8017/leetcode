// LeetCode 2131 - Longest Palindrome by Concatenating Two Letter Words
// https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

object Solution {
  def longestPalindrome(words: Array[String]): Int = {
    val freq = scala.collection.mutable.Map.empty[String, Int]
    words.foreach(w => freq(w) = freq.getOrElse(w, 0) + 1)
    var ans = 0
    var center = false
    freq.foreach { case (w, c) =>
      val rev = "" + w.charAt(1) + w.charAt(0)
      if (w.charAt(0) == w.charAt(1)) {
        ans += (c / 2) * 4
        if (c % 2 != 0) center = true
      } else if (w.compareTo(rev) < 0) {
        ans += math.min(c, freq.getOrElse(rev, 0)) * 4
      }
    }
    if (center) ans += 2
    ans
  }
}
