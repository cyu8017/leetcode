// LeetCode 3259 - Maximum Energy Boost From Two Drinks
// https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

object Solution {
  def maxEnergyBoost(energyDrinkA: Array[Int], energyDrinkB: Array[Int]): Long = {
    val n = energyDrinkA.length
    val dpA = new Array[Long](n)
    val dpB = new Array[Long](n)
    dpA(0) = energyDrinkA(0)
    dpB(0) = energyDrinkB(0)
    if (n == 1) return math.max(dpA(0), dpB(0))
    dpA(1) = energyDrinkA(1) + dpA(0)
    dpB(1) = energyDrinkB(1) + dpB(0)
    var i = 2
    while (i < n) {
      dpA(i) = energyDrinkA(i) + math.max(dpA(i - 1), dpB(i - 2))
      dpB(i) = energyDrinkB(i) + math.max(dpB(i - 1), dpA(i - 2))
      i += 1
    }
    math.max(dpA(n - 1), dpB(n - 1))
  }
}
