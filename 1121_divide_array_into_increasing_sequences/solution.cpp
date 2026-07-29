// LeetCode 1121 - Divide Array Into Increasing Sequences
// https://leetcode.com/problems/divide-array-into-increasing-sequences/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    bool canDivideIntoSubsequences(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> count;
        int maxFreq = 0;
        for (int x : nums) {
            maxFreq = std::max(maxFreq, ++count[x]);
        }
        return static_cast<int>(nums.size()) >= k * maxFreq;
    }
};
