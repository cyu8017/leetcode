// LeetCode 1134 - Armstrong Number
// https://leetcode.com/problems/armstrong-number/

#include <cmath>
#include <string>

class Solution {
public:
    bool isArmstrong(int n) {
        const std::string digits = std::to_string(n);
        const int power = static_cast<int>(digits.size());
        int sum = 0;
        for (char d : digits) sum += static_cast<int>(std::pow(d - '0', power));
        return sum == n;
    }
};
