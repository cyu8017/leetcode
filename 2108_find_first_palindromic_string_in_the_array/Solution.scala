// LeetCode 2108 - Find First Palindromic String in the Array
// https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

object Solution {
  def firstPalindrome(words: Array[String]): String = {
    words.find { w =>
      var l = 0
      var r = w.length - 1
      var ok = true
      while (l < r) {
        if (w.charAt(l) != w.charAt(r)) ok = false
        l += 1
        r -= 1
      }
      ok
    }.getOrElse("")
  }
}
