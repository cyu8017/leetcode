// LeetCode 0216 - Combination Sum III
// https://leetcode.com/problems/combination-sum-iii/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> combinationSum3(int k, int n) {
        std::vector<std::vector<int>> result;
        std::vector<int> path;
        backtrack(1, k, n, path, result);
        return result;
    }

private:
    void backtrack(
        int start,
        int k,
        int remaining,
        std::vector<int>& path,
        std::vector<std::vector<int>>& result
    ) {
        if (static_cast<int>(path.size()) == k) {
            if (remaining == 0) {
                result.push_back(path);
            }
            return;
        }
        if (remaining <= 0 || static_cast<int>(path.size()) >= k) {
            return;
        }

        for (int num = start; num <= 9; num++) {
            if (num > remaining) {
                break;
            }
            path.push_back(num);
            backtrack(num + 1, k, remaining - num, path, result);
            path.pop_back();
        }
    }
};
