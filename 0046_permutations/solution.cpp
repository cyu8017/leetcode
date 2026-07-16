// LeetCode 0046 - Permutations
// https://leetcode.com/problems/permutations/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> permute(std::vector<int>& nums) {
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
            used[i] = true;
            path.push_back(nums[i]);
            backtrack(nums, path, used, result);
            path.pop_back();
            used[i] = false;
        }
    }
};
