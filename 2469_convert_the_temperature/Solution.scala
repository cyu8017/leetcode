// LeetCode 2469 - Convert the Temperature
// https://leetcode.com/problems/convert-the-temperature/

object Solution {
  def convertTemperature(celsius: Double): Array[Double] = {
    Array(celsius + 273.15, celsius * 1.80 + 32.00)
  }
}
