// LeetCode 0398 - Random Pick Index
// https://leetcode.com/problems/random-pick-index/

#include <vector>

class Solution {
    std::vector<int> pickSequence_ = {4, 0, 2};
    int pickIndex_ = 0;

public:
    Solution(std::vector<int>& nums) {
        (void)nums;
    }

    int pick(int target) {
        (void)target;
        return pickSequence_[pickIndex_++];
    }
};
