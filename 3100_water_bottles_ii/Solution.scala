// LeetCode 3100 - Water Bottles II
// https://leetcode.com/problems/water-bottles-ii/

object Solution {
  def maxBottlesDrunk(numBottles0: Int, numExchange0: Int): Int = {
    var numBottles = numBottles0
    var numExchange = numExchange0
    var ans = numBottles
    while (numBottles >= numExchange) {
      numBottles -= numExchange
      numExchange += 1
      ans += 1
      numBottles += 1
    }
    ans
  }
}
