// LeetCode 0339 - Nested List Weight Sum
// https://leetcode.com/problems/nested-list-weight-sum/

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
        int total = 0;
        dfs(nestedList, 1, total);
        return total;
    }

private:
    void dfs(const std::vector<NestedInteger>& items, int depth, int& total) {
        for (const NestedInteger& item : items) {
            if (item.isInteger()) {
                total += item.getInteger() * depth;
            } else {
                dfs(item.getList(), depth + 1, total);
            }
        }
    }
};
