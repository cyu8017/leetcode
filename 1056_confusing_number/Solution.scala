// LeetCode 1056 - Confusing Number
// https://leetcode.com/problems/confusing-number/

object Solution {
  def confusingNumber(n: Int): Boolean = {
    val rotate = Map('0' -> '0', '1' -> '1', '6' -> '9', '8' -> '8', '9' -> '6')
    val s = n.toString
    val rotated = new StringBuilder
    for (ch <- s.reverse) {
      if (!rotate.contains(ch)) return false
      rotated.append(rotate(ch))
    }
    rotated.toString != s
  }
}
