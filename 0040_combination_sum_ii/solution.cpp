// LeetCode 0040 - Combination Sum II
// https://leetcode.com/problems/combination-sum-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> combinationSum2(std::vector<int>& candidates, int target) {
        std::sort(candidates.begin(), candidates.end());
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
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue;
            }
            path.push_back(candidates[i]);
            backtrack(candidates, remaining - candidates[i], i + 1, path, result);
            path.pop_back();
        }
    }
};
