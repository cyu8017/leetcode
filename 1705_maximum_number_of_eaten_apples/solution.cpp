// LeetCode 1705 - Maximum Number of Eaten Apples
// https://leetcode.com/problems/maximum-number-of-eaten-apples/

#include <functional>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int eatenApples(std::vector<int>& apples, std::vector<int>& days) {
        using Item = std::pair<int, int>;
        std::priority_queue<Item, std::vector<Item>, std::greater<Item>> heap;
        int n = static_cast<int>(apples.size());
        int day = 0;
        int eaten = 0;
        while (day < n || !heap.empty()) {
            if (day < n && apples[day] > 0) {
                heap.push({day + days[day], apples[day]});
            }
            while (!heap.empty() && heap.top().first <= day) {
                heap.pop();
            }
            if (!heap.empty()) {
                auto [expire, count] = heap.top();
                heap.pop();
                eaten++;
                if (count > 1) {
                    heap.push({expire, count - 1});
                }
            }
            day++;
        }
        return eaten;
    }
};
