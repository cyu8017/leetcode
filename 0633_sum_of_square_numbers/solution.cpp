// LeetCode 0633 - Sum of Square Numbers
// https://leetcode.com/problems/sum-of-square-numbers/

#include <cmath>

class Solution {
public:
    bool judgeSquareSum(int c) {
        long long left = 0;
        long long right = static_cast<long long>(std::sqrt(c));
        while (left <= right) {
            const long long total = left * left + right * right;
            if (total == c) {
                return true;
            }
            if (total < c) {
                ++left;
            } else {
                --right;
            }
        }
        return false;
    }
};
