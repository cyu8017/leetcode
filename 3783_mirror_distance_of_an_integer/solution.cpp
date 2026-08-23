// LeetCode 3783 - Mirror Distance Of An Integer
// https://leetcode.com/problems/mirror-distance-of-an-integer/

#include <cstdlib>

class Solution {
public:
    int mirrorDistance(int n) {
        auto reverse = [](int x) {
            int y = 0;
            for (; x > 0; x /= 10) y = y * 10 + x % 10;
            return y;
        };
        return std::abs(n - reverse(n));
    }
};
