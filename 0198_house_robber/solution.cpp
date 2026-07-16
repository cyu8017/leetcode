// LeetCode 0198 - House Robber
// https://leetcode.com/problems/house-robber/

#include <algorithm>
#include <vector>

class Solution {
public:
    int rob(std::vector<int>& nums) {
        int previous_two = 0;
        int previous_one = 0;
        for (int value : nums) {
            const int current = std::max(previous_one, previous_two + value);
            previous_two = previous_one;
            previous_one = current;
        }
        return previous_one;
    }
};
