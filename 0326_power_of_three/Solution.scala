// LeetCode 0326 - Power of Three

// https://leetcode.com/problems/power-of-three/



object Solution {

  def isPowerOfThree(n: Int): Boolean = {

    if (n <= 0) {

      return false

    }

    var value = n

    while (value % 3 == 0) {

      value /= 3

    }

    value == 1

  }

}

