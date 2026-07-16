// LeetCode 0389 - Find the Difference

// https://leetcode.com/problems/find-the-difference/



object Solution {

  def findTheDifference(s: String, t: String): Char = {

    var xorValue = 0

    for (ch <- s) {

      xorValue ^= ch.toInt

    }

    for (ch <- t) {

      xorValue ^= ch.toInt

    }

    xorValue.toChar

  }

}
