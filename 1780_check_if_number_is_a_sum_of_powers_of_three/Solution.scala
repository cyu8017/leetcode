// LeetCode 1780 - Check if Number is a Sum of Powers of Three
// https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

object Solution {
  def checkPowersOfThree(n: Int): Boolean = {
    var value = n
    while (value > 0) {
      if (value % 3 == 2) {
        return false
      }
      value /= 3
    }
    true
  }
}
