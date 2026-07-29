// LeetCode 0594 - Longest Harmonious Subsequence
// https://leetcode.com/problems/longest-harmonious-subsequence/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int findLHS(std::vector<int>& nums) {
        std::unordered_map<int, int> counts;
        for (int num : nums) {
            ++counts[num];
        }
        int best = 0;
        for (const auto& [value, count] : counts) {
            auto it = counts.find(value + 1);
            if (it != counts.end()) {
                best = std::max(best, count + it->second);
            }
        }
        return best;
    }
};
