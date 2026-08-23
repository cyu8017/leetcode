// LeetCode 0364 - Nested List Weight Sum II
// https://leetcode.com/problems/nested-list-weight-sum-ii/

#include <algorithm>
#include <utility>
#include <vector>

class NestedInteger {
public:
    NestedInteger() : isInteger_(false), integer_(0) {}
    NestedInteger(int value) : isInteger_(true), integer_(value) {}

    bool isInteger() const {
        return isInteger_;
    }

    int getInteger() const {
        return integer_;
    }

    const std::vector<NestedInteger>& getList() const {
        return list_;
    }

    std::vector<NestedInteger>& getList() {
        return list_;
    }

private:
    bool isInteger_;
    int integer_;
    std::vector<NestedInteger> list_;
};

class Solution {
public:
    int depthSum(const std::vector<NestedInteger>& nestedList) {
        std::vector<std::pair<int, int>> weighted;

        dfs(nestedList, 1, weighted);
        if (weighted.empty()) {
            return 0;
        }

        int maxDepth = 0;
        for (const auto& entry : weighted) {
            maxDepth = std::max(maxDepth, entry.second);
        }

        int total = 0;
        for (const auto& entry : weighted) {
            total += entry.first * (maxDepth - entry.second + 1);
        }

        return total;
    }

private:
    void dfs(const std::vector<NestedInteger>& items, int depth, std::vector<std::pair<int, int>>& weighted) {
        for (const NestedInteger& item : items) {
            if (item.isInteger()) {
                weighted.push_back({item.getInteger(), depth});
            } else {
                dfs(item.getList(), depth + 1, weighted);
            }
        }
    }
};
