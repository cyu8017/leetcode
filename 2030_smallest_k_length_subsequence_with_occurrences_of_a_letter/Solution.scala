// LeetCode 2030 - Smallest K-Length Subsequence With Occurrences of a Letter
// https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/

object Solution {
  def smallestSubsequence(s: String, k: Int, letter: Char, repetition: Int): String = {
    val n = s.length
    var remainLetter = 0
    s.foreach { c => if (c == letter) remainLetter += 1 }
    val stack = new StringBuilder
    var inStackLetter = 0
    var i = 0
    while (i < n) {
      val ch = s.charAt(i)
      var stop = false
      while (!stop && stack.nonEmpty && ch < stack.charAt(stack.length - 1) && stack.length + n - i > k) {
        val top = stack.charAt(stack.length - 1)
        if (top == letter) {
          if (inStackLetter + remainLetter - 1 < repetition) stop = true
          else inStackLetter -= 1
        }
        if (!stop) stack.setLength(stack.length - 1)
      }
      if (stack.length < k) {
        if (ch == letter) { stack.append(ch); inStackLetter += 1 }
        else if (k - stack.length > repetition - inStackLetter) stack.append(ch)
      }
      if (ch == letter) remainLetter -= 1
      i += 1
    }
    stack.toString
  }
}
