// LeetCode 0047 - Permutations II
// https://leetcode.com/problems/permutations-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> permuteUnique(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> result;
        std::vector<int> path;
        std::vector<bool> used(nums.size(), false);
        backtrack(nums, path, used, result);
        return result;
    }

private:
    void backtrack(
        std::vector<int>& nums,
        std::vector<int>& path,
        std::vector<bool>& used,
        std::vector<std::vector<int>>& result
    ) {
        if (path.size() == nums.size()) {
            result.push_back(path);
            return;
        }

        for (int i = 0; i < static_cast<int>(nums.size()); i++) {
            if (used[i]) {
                continue;
            }
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
                continue;
            }
            used[i] = true;
            path.push_back(nums[i]);
            backtrack(nums, path, used, result);
            path.pop_back();
            used[i] = false;
        }
    }
};
