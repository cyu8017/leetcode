// LeetCode 1834 - Single-Threaded CPU
// https://leetcode.com/problems/single-threaded-cpu/

#include <algorithm>
#include <functional>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> getOrder(std::vector<std::vector<int>>& tasks) {
        int n = static_cast<int>(tasks.size());
        std::vector<std::pair<std::pair<int, int>, int>> indexed;
        indexed.reserve(n);
        for (int i = 0; i < n; ++i) {
            indexed.push_back({{tasks[i][0], tasks[i][1]}, i});
        }
        std::sort(indexed.begin(), indexed.end(), [](const auto& a, const auto& b) {
            if (a.first.first != b.first.first) {
                return a.first.first < b.first.first;
            }
            return a.second < b.second;
        });

        using Node = std::pair<int, int>;
        std::priority_queue<Node, std::vector<Node>, std::greater<>> heap;
        std::vector<int> order;
        long long time = 0;
        int i = 0;
        while (i < n || !heap.empty()) {
            if (i < n && heap.empty()) {
                time = std::max(time, static_cast<long long>(indexed[i].first.first));
            }
            while (i < n && indexed[i].first.first <= time) {
                heap.push({indexed[i].first.second, indexed[i].second});
                ++i;
            }
            auto [duration, idx] = heap.top();
            heap.pop();
            time += duration;
            order.push_back(idx);
        }
        return order;
    }
};
