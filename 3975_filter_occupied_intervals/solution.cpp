// LeetCode 3975 - Filter Occupied Intervals
// https://leetcode.com/problems/filter-occupied-intervals/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> filterOccupiedIntervals(std::vector<std::vector<int>>& occupiedIntervals, int freeStart, int freeEnd) {
        std::sort(occupiedIntervals.begin(), occupiedIntervals.end(), [](auto& a, auto& b) {
            return a[0] < b[0];
        });
        std::vector<std::vector<int>> busy = {occupiedIntervals[0]};
        for (int i = 1; i < (int)occupiedIntervals.size(); i++) {
            auto& cur = occupiedIntervals[i];
            auto& last = busy.back();
            if (last[1] + 1 < cur[0]) busy.push_back(cur);
            else if (cur[1] > last[1]) last[1] = cur[1];
        }
        std::vector<std::vector<int>> ans;
        for (auto& it : busy) {
            int s = it[0], e = it[1];
            if (e < freeStart || s > freeEnd) ans.push_back({s, e});
            else {
                if (s < freeStart) ans.push_back({s, freeStart - 1});
                if (e > freeEnd) ans.push_back({freeEnd + 1, e});
            }
        }
        return ans;
    }
};
