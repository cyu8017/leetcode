// LeetCode 2259 - Remove Digit From Number to Maximize Result
// https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

object Solution {
  def removeDigit(number: String, digit: Char): String = {
    var best = ""
    var i = 0
    while (i < number.length) {
      if (number.charAt(i) == digit) {
        val cand = number.substring(0, i) + number.substring(i + 1)
        if (cand.compareTo(best) > 0) best = cand
      }
      i += 1
    }
    best
  }
}
