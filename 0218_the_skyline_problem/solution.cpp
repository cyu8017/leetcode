// LeetCode 0218 - The Skyline Problem
// https://leetcode.com/problems/the-skyline-problem/

#include <algorithm>
#include <climits>
#include <queue>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> getSkyline(std::vector<std::vector<int>>& buildings) {
        std::vector<std::tuple<int, int, int>> events;
        for (const auto& building : buildings) {
            events.emplace_back(building[0], -building[2], building[1]);
            events.emplace_back(building[1], 0, 0);
        }
        std::sort(events.begin(), events.end());

        std::vector<std::vector<int>> result;
        using Item = std::pair<int, int>;
        auto cmp = [](const Item& a, const Item& b) { return a.first > b.first; };
        std::priority_queue<Item, std::vector<Item>, decltype(cmp)> live(cmp);
        live.push({0, INT32_MAX});

        for (const auto& [x, negH, end] : events) {
            while (!live.empty() && live.top().second <= x) {
                live.pop();
            }
            if (negH != 0) {
                live.push({negH, end});
            }
            int height = -live.top().first;
            if (result.empty() || result.back()[1] != height) {
                result.push_back({x, height});
            }
        }
        return result;
    }
};
