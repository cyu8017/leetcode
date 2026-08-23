// LeetCode 0039 - Combination Sum
// https://leetcode.com/problems/combination-sum/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> combinationSum(std::vector<int>& candidates, int target) {
        std::vector<std::vector<int>> result;
        std::vector<int> path;
        backtrack(candidates, target, 0, path, result);
        return result;
    }

private:
    void backtrack(
        const std::vector<int>& candidates,
        int remaining,
        int start,
        std::vector<int>& path,
        std::vector<std::vector<int>>& result
    ) {
        if (remaining == 0) {
            result.push_back(path);
            return;
        }
        if (remaining < 0) {
            return;
        }

        for (int i = start; i < static_cast<int>(candidates.size()); i++) {
            path.push_back(candidates[i]);
            backtrack(candidates, remaining - candidates[i], i, path, result);
            path.pop_back();
        }
    }
};
