// LeetCode 3899 - Angles Of A Triangle
// https://leetcode.com/problems/angles-of-a-triangle/

#include <algorithm>
#include <cmath>
#include <vector>

class Solution {
public:
    std::vector<double> internalAngles(std::vector<int>& sides) {
        std::sort(sides.begin(), sides.end());
        int a = sides[0], b = sides[1], c = sides[2];
        if (a + b <= c) return {};
        const double PI = std::acos(-1.0);
        double A = std::acos((double)(b * b + c * c - a * a) / (2.0 * b * c)) * 180.0 / PI;
        double B = std::acos((double)(a * a + c * c - b * b) / (2.0 * a * c)) * 180.0 / PI;
        double C = 180.0 - A - B;
        return {A, B, C};
    }
};
