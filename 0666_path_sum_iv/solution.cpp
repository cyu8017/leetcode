// LeetCode 0666 - Path Sum IV
// https://leetcode.com/problems/path-sum-iv/

#include <map>
#include <utility>
#include <vector>

class Solution {
    std::map<std::pair<int, int>, int> tree_;
    int total_ = 0;

    void dfs(int depth, int pos, int path) {
        if (!tree_.count({depth, pos})) {
            return;
        }
        path += tree_[{depth, pos}];
        const auto left = std::make_pair(depth + 1, pos * 2 - 1);
        const auto right = std::make_pair(depth + 1, pos * 2);
        if (!tree_.count(left) && !tree_.count(right)) {
            total_ += path;
            return;
        }
        dfs(depth + 1, pos * 2 - 1, path);
        dfs(depth + 1, pos * 2, path);
    }

public:
    int pathSum(std::vector<int>& nums) {
        tree_.clear();
        total_ = 0;
        for (int num : nums) {
            tree_[{num / 100, (num / 10) % 10}] = num % 10;
        }
        dfs(1, 1, 0);
        return total_;
    }
};
