// LeetCode 1518 - Water Bottles
// https://leetcode.com/problems/water-bottles/

object Solution {
  def numWaterBottles(numBottles: Int, numExchange: Int): Int = {
    var bottles = numBottles
    var total = numBottles
    while (bottles >= numExchange) {
      val neu = bottles / numExchange
      val rem = bottles % numExchange
      total += neu
      bottles = neu + rem
    }
    total
  }
}
