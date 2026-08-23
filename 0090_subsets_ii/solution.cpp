// LeetCode 0090 - Subsets II
// https://leetcode.com/problems/subsets-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> subsetsWithDup(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> result;
        std::vector<int> path;
        backtrack(nums, 0, path, result);
        return result;
    }

private:
    void backtrack(
        const std::vector<int>& nums,
        int start,
        std::vector<int>& path,
        std::vector<std::vector<int>>& result
    ) {
        result.push_back(path);
        for (int i = start; i < static_cast<int>(nums.size()); i++) {
            if (i > start && nums[i] == nums[i - 1]) {
                continue;
            }
            path.push_back(nums[i]);
            backtrack(nums, i + 1, path, result);
            path.pop_back();
        }
    }
};
