// LeetCode 0134 - Gas Station
// https://leetcode.com/problems/gas-station/

object Solution {
  def canCompleteCircuit(gas: Array[Int], cost: Array[Int]): Int = {
    var total = 0
    var tank = 0
    var start = 0
    for (i <- gas.indices) {
      val diff = gas(i) - cost(i)
      total += diff
      tank += diff
      if (tank < 0) { start = i + 1; tank = 0 }
    }
    if (total >= 0) start else -1
  }
}
