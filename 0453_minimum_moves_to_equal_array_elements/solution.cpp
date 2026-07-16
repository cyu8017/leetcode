// LeetCode 0453 - Minimum Moves to Equal Array Elements
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minMoves(std::vector<int>& nums) {
        int minimum = *std::min_element(nums.begin(), nums.end());
        int total = 0;
        for (int value : nums) {
            total += value - minimum;
        }
        return total;
    }
};
