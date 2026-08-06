// LeetCode 1952 - Three Divisors
// https://leetcode.com/problems/three-divisors/

object Solution {
  def isThree(n: Int): Boolean = {
    val root = math.sqrt(n).toInt
    if (root * root != n || root < 2) return false
    var i = 2
    while (i * i <= root) {
      if (root % i == 0) return false
      i += 1
    }
    true
  }
}
