// LeetCode 2469 - Convert the Temperature
// https://leetcode.com/problems/convert-the-temperature/

public class Solution {
    public double[] ConvertTemperature(double celsius) {
        return new double[] { celsius + 273.15, celsius * 1.80 + 32.00 };
    }
}
