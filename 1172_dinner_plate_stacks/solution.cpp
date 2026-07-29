// LeetCode 1172 - Dinner Plate Stacks
// https://leetcode.com/problems/dinner-plate-stacks/

#include <queue>
#include <vector>

class DinnerPlates {
public:
    DinnerPlates(int capacity) : capacity(capacity) {}

    void push(int val) {
        while (!available.empty() &&
               (available.top() >= static_cast<int>(stacks.size()) ||
                static_cast<int>(stacks[available.top()].size()) == capacity)) {
            available.pop();
        }
        if (available.empty()) {
            stacks.emplace_back();
            available.push(static_cast<int>(stacks.size()) - 1);
        }
        int idx = available.top();
        stacks[idx].push_back(val);
        if (static_cast<int>(stacks[idx].size()) == capacity) available.pop();
    }

    int pop() {
        while (!stacks.empty() && stacks.back().empty()) stacks.pop_back();
        return stacks.empty() ? -1 : popAtStack(static_cast<int>(stacks.size()) - 1);
    }

    int popAtStack(int index) {
        if (index < 0 || index >= static_cast<int>(stacks.size()) || stacks[index].empty()) return -1;
        if (static_cast<int>(stacks[index].size()) == capacity) available.push(index);
        int val = stacks[index].back();
        stacks[index].pop_back();
        return val;
    }

private:
    int capacity;
    std::vector<std::vector<int>> stacks;
    std::priority_queue<int, std::vector<int>, std::greater<int>> available;
};
