// LeetCode 2264 - Largest 3-Same-Digit Number in String
// https://leetcode.com/problems/largest-3-same-digit-number-in-string/

object Solution {
  def largestGoodInteger(num: String): String = {
    var best = ""
    var i = 0
    while (i + 2 < num.length) {
      if (num.charAt(i) == num.charAt(i + 1) && num.charAt(i) == num.charAt(i + 2)) {
        val cand = num.substring(i, i + 3)
        if (cand.compareTo(best) > 0) best = cand
      }
      i += 1
    }
    best
  }
}
