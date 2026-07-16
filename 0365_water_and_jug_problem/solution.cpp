// LeetCode 0365 - Water and Jug Problem
// https://leetcode.com/problems/water-and-jug-problem/

#include <numeric>

class Solution {
public:
    bool canMeasureWater(int x, int y, int target) {
        if (target == 0) {
            return true;
        }
        if (x + y < target) {
            return false;
        }
        return target % std::gcd(x, y) == 0;
    }
};
