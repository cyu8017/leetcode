// LeetCode 2733 - Neither Minimum nor Maximum
// https://leetcode.com/problems/neither-minimum-nor-maximum/

#include <vector>
#include <algorithm>

class Solution {
public:
    int findNonMinOrMax(std::vector<int>& nums) {
        if ((int)nums.size() < 3) return -1;
        int a = nums[0], b = nums[1], c = nums[2];
        return a + b + c - std::max({a, b, c}) - std::min({a, b, c});
    }
};
