// LeetCode 0716 - Max Stack
// https://leetcode.com/problems/max-stack/

#include <algorithm>
#include <vector>

class MaxStack {
public:
    MaxStack() = default;

    void push(int x) {
        stack_.push_back(x);
        maxes_.push_back(maxes_.empty() ? x : std::max(x, maxes_.back()));
    }

    int pop() {
        maxes_.pop_back();
        int val = stack_.back();
        stack_.pop_back();
        return val;
    }

    int top() { return stack_.back(); }

    int peekMax() { return maxes_.back(); }

    int popMax() {
        int maxVal = peekMax();
        std::vector<int> buffer;
        while (top() != maxVal) {
            buffer.push_back(pop());
        }
        pop();
        while (!buffer.empty()) {
            push(buffer.back());
            buffer.pop_back();
        }
        return maxVal;
    }

private:
    std::vector<int> stack_;
    std::vector<int> maxes_;
};
