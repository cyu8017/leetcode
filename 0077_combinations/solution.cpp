// LeetCode 0077 - Combinations
// https://leetcode.com/problems/combinations/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> combine(int n, int k) {
        std::vector<std::vector<int>> result;
        std::vector<int> path;
        backtrack(n, k, 1, path, result);
        return result;
    }

private:
    void backtrack(
        int n,
        int k,
        int start,
        std::vector<int>& path,
        std::vector<std::vector<int>>& result
    ) {
        if (static_cast<int>(path.size()) == k) {
            result.push_back(path);
            return;
        }

        int remaining = k - static_cast<int>(path.size());
        for (int i = start; i <= n - remaining + 1; i++) {
            path.push_back(i);
            backtrack(n, k, i + 1, path, result);
            path.pop_back();
        }
    }
};
