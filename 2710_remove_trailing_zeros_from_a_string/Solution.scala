// LeetCode 2710 - Remove Trailing Zeros From a String
// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

object Solution {
  def removeTrailingZeros(num: String): String = {
    var end = num.length
    while (end > 0 && num.charAt(end - 1) == '0') end -= 1
    num.substring(0, end)
  }
}
