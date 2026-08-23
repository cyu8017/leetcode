// LeetCode 0300 - Longest Increasing Subsequence
// https://leetcode.com/problems/longest-increasing-subsequence/

#include <algorithm>
#include <vector>

class Solution {
public:
    int lengthOfLIS(std::vector<int>& nums) {
        std::vector<int> piles;
        for (int num : nums) {
            auto iterator = std::lower_bound(piles.begin(), piles.end(), num);
            if (iterator == piles.end()) {
                piles.push_back(num);
            } else {
                *iterator = num;
            }
        }
        return static_cast<int>(piles.size());
    }
};
