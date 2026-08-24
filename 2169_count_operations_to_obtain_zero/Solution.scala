// LeetCode 2169 - Count Operations to Obtain Zero
// https://leetcode.com/problems/count-operations-to-obtain-zero/

object Solution {
  def countOperations(num1: Int, num2: Int): Int = {
    var a = num1
    var b = num2
    var ans = 0
    while (a > 0 && b > 0) {
      if (a >= b) { ans += a / b; a %= b }
      else { ans += b / a; b %= a }
    }
    ans
  }
}
