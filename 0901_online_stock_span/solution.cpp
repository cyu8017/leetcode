// LeetCode 0901 - Online Stock Span
// https://leetcode.com/problems/online-stock-span/

#include <utility>
#include <vector>

class StockSpanner {
public:
    StockSpanner() {}

    int next(int price) {
        int span = 1;
        while (!stack.empty() && stack.back().first <= price) {
            span += stack.back().second;
            stack.pop_back();
        }
        stack.emplace_back(price, span);
        return span;
    }

private:
    std::vector<std::pair<int, int>> stack;
};
