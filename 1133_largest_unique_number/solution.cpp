// LeetCode 1133 - Largest Unique Number
// https://leetcode.com/problems/largest-unique-number/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int largestUniqueNumber(std::vector<int>& nums) {
        std::unordered_map<int, int> count;
        for (int x : nums) ++count[x];
        int ans = -1;
        for (const auto& [value, freq] : count) if (freq == 1) ans = std::max(ans, value);
        return ans;
    }
};
