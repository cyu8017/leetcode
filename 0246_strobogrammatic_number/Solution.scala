// LeetCode 0246 - Strobogrammatic Number
// https://leetcode.com/problems/strobogrammatic-number/

object Solution {
  def isStrobogrammatic(num: String): Boolean = {
    val mapping = Map('0' -> '0', '1' -> '1', '6' -> '9', '8' -> '8', '9' -> '6')
    var left = 0
    var right = num.length - 1
    while (left <= right) {
      if (mapping.get(num(left)) != Some(num(right))) {
        return false
      }
      left += 1
      right -= 1
    }
    true
  }
}
