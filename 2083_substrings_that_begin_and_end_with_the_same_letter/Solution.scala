// LeetCode 2083 - Substrings That Begin and End With the Same Letter
// https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/

object Solution {
  def numberOfSubstrings(s: String): Long = {
    val freq = Array.ofDim[Long](26)
    var ans = 0L
    s.foreach { c =>
      freq(c - 'a') += 1
      ans += freq(c - 'a')
    }
    ans
  }
}
