// LeetCode 0341 - Flatten Nested List Iterator
// https://leetcode.com/problems/flatten-nested-list-iterator/

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

class NestedIterator {
    struct Frame {
        NestedInteger* node;
        int index;
    };

    std::vector<Frame> stack_;

    void prepareNext() {
        while (!stack_.empty()) {
            NestedInteger* current = stack_.back().node;
            int index = stack_.back().index;
            if (current->isInteger()) {
                return;
            }
            const std::vector<NestedInteger>& nested = current->getList();
            if (index >= static_cast<int>(nested.size())) {
                stack_.pop_back();
                continue;
            }
            stack_.back().index = index + 1;
            stack_.push_back({const_cast<NestedInteger*>(&nested[index]), 0});
        }
    }

    int advance(const std::vector<NestedInteger>& nested) {
        for (int index = static_cast<int>(nested.size()) - 1; index >= 0; --index) {
            stack_.push_back({const_cast<NestedInteger*>(&nested[index]), 0});
        }
        prepareNext();
        NestedInteger* current = stack_.back().node;
        stack_.pop_back();
        if (current->isInteger()) {
            return current->getInteger();
        }
        return advance(current->getList());
    }

public:
    NestedIterator(std::vector<NestedInteger>& nestedList) {
        for (int index = static_cast<int>(nestedList.size()) - 1; index >= 0; --index) {
            stack_.push_back({&nestedList[index], 0});
        }
    }

    int next() {
        NestedInteger* current = stack_.back().node;
        stack_.pop_back();
        if (current->isInteger()) {
            return current->getInteger();
        }
        return advance(current->getList());
    }

    bool hasNext() {
        prepareNext();
        return !stack_.empty();
    }
};
