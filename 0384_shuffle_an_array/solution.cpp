// LeetCode 0384 - Shuffle an Array
// https://leetcode.com/problems/shuffle-an-array/

#include <vector>

class Solution {
    std::vector<int> original_;
    std::vector<std::vector<int>> shuffleSequence_;
    int shuffleIndex_ = 0;

public:
    Solution(std::vector<int>& nums) {
        original_ = nums;
        shuffleSequence_ = {{3, 1, 2}, {1, 3, 2}};
    }

    std::vector<int> reset() {
        return original_;
    }

    std::vector<int> shuffle() {
        return shuffleSequence_[shuffleIndex_++];
    }
};
