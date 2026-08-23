// LeetCode 0850 - Rectangle Area II
// https://leetcode.com/problems/rectangle-area-ii/

#include <algorithm>
#include <tuple>
#include <vector>

class Solution {
public:
    int rectangleArea(std::vector<std::vector<int>>& rectangles) {
        const int MOD = 1'000'000'007;
        std::vector<std::tuple<int, int, int, int>> events;
        for (auto& r : rectangles) {
            events.emplace_back(r[0], 1, r[1], r[3]);
            events.emplace_back(r[2], -1, r[1], r[3]);
        }
        std::sort(events.begin(), events.end());

        auto coveredLength = [](std::vector<std::pair<int, int>> active) {
            if (active.empty()) {
                return 0;
            }
            std::sort(active.begin(), active.end());
            int total = 0;
            int curStart = active[0].first, curEnd = active[0].second;
            for (size_t i = 1; i < active.size(); ++i) {
                int start = active[i].first, end = active[i].second;
                if (start > curEnd) {
                    total += curEnd - curStart;
                    curStart = start;
                    curEnd = end;
                } else {
                    curEnd = std::max(curEnd, end);
                }
            }
            total += curEnd - curStart;
            return total;
        };

        std::vector<std::pair<int, int>> active;
        long long area = 0;
        int prevX = std::get<0>(events[0]);
        for (auto [x, typ, y1, y2] : events) {
            area += static_cast<long long>(coveredLength(active)) * (x - prevX);
            if (typ == 1) {
                active.emplace_back(y1, y2);
            } else {
                active.erase(
                    std::find(active.begin(), active.end(), std::make_pair(y1, y2)));
            }
            prevX = x;
        }
        return static_cast<int>(area % MOD);
    }
};
