// LeetCode 1221 - Split a String in Balanced Strings
// https://leetcode.com/problems/split-a-string-in-balanced-strings/

object Solution {
  def balancedStringSplit(s: String): Int = {
    var balance = 0
    var answer = 0
    for (ch <- s) {
      balance += (if (ch == 'L') 1 else -1)
      if (balance == 0) answer += 1
    }
    answer
  }
}
