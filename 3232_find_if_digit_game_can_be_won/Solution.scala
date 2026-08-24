// LeetCode 3232 - Find if Digit Game Can Be Won
// https://leetcode.com/problems/find-if-digit-game-can-be-won/

object Solution {
  def canAliceWin(nums: Array[Int]): Boolean = {
    var a = 0
    var b = 0
    for (x <- nums) {
      if (x < 10) a += x else b += x
    }
    a != b
  }
}
