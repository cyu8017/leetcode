// LeetCode 3723 - Maximize Sum Of Squares Of Digits
// https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

object Solution {
  def maxSumOfSquares(num: Int, sum: Int): String = {
    if (num * 9 < sum) return ""
    val k = sum / 9
    val s = sum % 9
    val ans = new StringBuilder
    var i = 0
    while (i < k) {
      ans.append('9')
      i += 1
    }
    if (s > 0) ans.append(('0' + s).toChar)
    while (ans.length < num) ans.append('0')
    ans.toString
  }
}
