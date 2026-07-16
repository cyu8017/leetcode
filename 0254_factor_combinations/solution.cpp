// LeetCode 0254 - Factor Combinations
// https://leetcode.com/problems/factor-combinations/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> getFactors(int n) {
        std::vector<std::vector<int>> result;
        std::vector<int> path;
        backtrack(n, 2, path, result);
        return result;
    }

private:
    void backtrack(int remain, int start, std::vector<int>& path, std::vector<std::vector<int>>& result) {
        if (start > remain) {
            if (path.size() > 1) {
                result.push_back(path);
            }
            return;
        }

        for (int factor = start; factor * factor <= remain; factor++) {
            if (remain % factor == 0) {
                path.push_back(factor);
                backtrack(remain / factor, factor, path, result);
                path.pop_back();
            }
        }

        if (!path.empty()) {
            path.push_back(remain);
            if (path.size() > 1) {
                result.push_back(path);
            }
            path.pop_back();
        }
    }
};
