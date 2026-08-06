// LeetCode 1134 - Armstrong Number
// https://leetcode.com/problems/armstrong-number/

object Solution {
  def isArmstrong(n: Int): Boolean = {
    val s = n.toString
    val k = s.length
    s.map(c => math.pow(c - '0', k).toInt).sum == n
  }
}
