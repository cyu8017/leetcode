// LeetCode 2469 - Convert the Temperature
// https://leetcode.com/problems/convert-the-temperature/

class Solution {
    fun convertTemperature(celsius: Double): DoubleArray {
        return doubleArrayOf(celsius + 273.15, celsius * 1.80 + 32.00)
    }
}
