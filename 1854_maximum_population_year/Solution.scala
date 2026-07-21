// LeetCode 1854 - Maximum Population Year
// https://leetcode.com/problems/maximum-population-year/

object Solution {
  def maximumPopulation(logs: Array[Array[Int]]): Int = {
    val diff = Array.fill(101)(0)
    for (log <- logs) {
      diff(log(0) - 1950) += 1
      diff(log(1) - 1950) -= 1
    }
    var bestYear = 1950
    var bestPopulation = 0
    var population = 0
    for (offset <- 0 until 101) {
      population += diff(offset)
      if (population > bestPopulation) {
        bestPopulation = population
        bestYear = 1950 + offset
      }
    }
    bestYear
  }
}
