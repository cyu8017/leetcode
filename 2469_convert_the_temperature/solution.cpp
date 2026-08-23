// LeetCode 2469 - Convert the Temperature
// https://leetcode.com/problems/convert-the-temperature/

#include <vector>

class Solution {
public:
    std::vector<double> convertTemperature(double celsius) {
        return {celsius + 273.15, celsius * 1.80 + 32.00};
    }
};
