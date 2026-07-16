// LeetCode 0342 - Power of Four

// https://leetcode.com/problems/power-of-four/



object Solution {

  def isPowerOfFour(n: Int): Boolean = {

    n > 0 && (n & (n - 1)) == 0 && n % 3 == 1

  }

}
