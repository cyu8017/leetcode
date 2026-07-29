// LeetCode 0754 - Reach a Number
// https://leetcode.com/problems/reach-a-number/

#include <cstdlib>

class Solution {
public:
    int reachNumber(int target) {
        target = std::abs(target);
        int steps = 0;
        int total = 0;
        while (total < target || (total - target) % 2) {
            ++steps;
            total += steps;
        }
        return steps;
    }
};
