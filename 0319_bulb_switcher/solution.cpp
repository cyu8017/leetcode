// LeetCode 0319 - Bulb Switcher
// https://leetcode.com/problems/bulb-switcher/

#include <cmath>

class Solution {
public:
    int bulbSwitch(int n) {
        return static_cast<int>(std::sqrt(n));
    }
};
