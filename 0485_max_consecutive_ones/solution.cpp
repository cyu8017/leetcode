// LeetCode 0485 - Max Consecutive Ones
// https://leetcode.com/problems/max-consecutive-ones/

#include <algorithm>
#include <vector>

class Solution {
public:
    int findMaxConsecutiveOnes(std::vector<int>& nums) {
        int best = 0;
        int current = 0;
        for (int num : nums) {
            if (num == 1) {
                ++current;
                best = std::max(best, current);
            } else {
                current = 0;
            }
        }
        return best;
    }
};
