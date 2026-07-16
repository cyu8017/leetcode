// LeetCode 0491 - Non-decreasing Subsequences
// https://leetcode.com/problems/non-decreasing-subsequences/

#include <algorithm>
#include <set>
#include <vector>

class Solution {
    std::set<std::vector<int>> result_;

    void backtrack(const std::vector<int>& nums, int start, std::vector<int>& path) {
        if (path.size() >= 2) {
            result_.insert(path);
        }
        std::set<int> used;
        for (int index = start; index < static_cast<int>(nums.size()); ++index) {
            if (used.count(nums[index]) > 0) {
                continue;
            }
            if (!path.empty() && nums[index] < path.back()) {
                continue;
            }
            used.insert(nums[index]);
            path.push_back(nums[index]);
            backtrack(nums, index + 1, path);
            path.pop_back();
        }
    }

public:
    std::vector<std::vector<int>> findSubsequences(std::vector<int>& nums) {
        result_.clear();
        std::vector<int> path;
        backtrack(nums, 0, path);
        return std::vector<std::vector<int>>(result_.begin(), result_.end());
    }
};
