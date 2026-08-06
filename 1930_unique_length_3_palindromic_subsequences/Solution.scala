// LeetCode 1930 - Unique Length-3 Palindromic Subsequences
// https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

object Solution {
  def countPalindromicSubsequence(s: String): Int = {
    val first = Array.fill(26)(-1)
    val last = Array.fill(26)(-1)
    for (i <- s.indices) {
      val c = s.charAt(i) - 'a'
      if (first(c) == -1) first(c) = i
      last(c) = i
    }
    var ans = 0
    for (c <- 0 until 26 if first(c) != -1 && last(c) - first(c) > 1) {
      val mid = scala.collection.mutable.Set.empty[Char]
      for (i <- first(c) + 1 until last(c)) mid += s.charAt(i)
      ans += mid.size
    }
    ans
  }
}
