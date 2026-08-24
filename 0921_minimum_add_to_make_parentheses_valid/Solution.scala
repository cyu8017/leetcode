// LeetCode 0921 - Minimum Add to Make Parentheses Valid
// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

object Solution {
  def minAddToMakeValid(s: String): Int = {
    var openNeed = 0
    var closeNeed = 0
    s.foreach { ch =>
      if (ch == '(') closeNeed += 1
      else if (closeNeed > 0) closeNeed -= 1
      else openNeed += 1
    }
    openNeed + closeNeed
  }
}
