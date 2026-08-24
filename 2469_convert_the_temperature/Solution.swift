// LeetCode 2469 - Convert the Temperature
// https://leetcode.com/problems/convert-the-temperature/

class Solution {
    func convertTemperature(_ celsius: Double) -> [Double] {
        [celsius + 273.15, celsius * 1.80 + 32.00]
    }
}
