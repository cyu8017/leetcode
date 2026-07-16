// LeetCode 0365 - Water and Jug Problem

// https://leetcode.com/problems/water-and-jug-problem/



object Solution {

  def canMeasureWater(x: Int, y: Int, target: Int): Boolean = {

    if (target == 0) return true

    if (x + y < target) return false

    target % gcd(x, y) == 0

  }



  private def gcd(a: Int, b: Int): Int = {

    var x = a

    var y = b

    while (y != 0) {

      val temp = y

      y = x % y

      x = temp

    }

    x

  }

}
