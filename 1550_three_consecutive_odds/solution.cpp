// LeetCode 1550 - Three Consecutive Odds
// https://leetcode.com/problems/three-consecutive-odds/

#include <vector>

class Solution {
public:
    bool threeConsecutiveOdds(std::vector<int>& arr) {
        int run = 0;
        for (int value : arr) {
            run = (value & 1) ? run + 1 : 0;
            if (run == 3) {
                return true;
            }
        }
        return false;
    }
};
