// LeetCode 2940 - Find Building Where Alice and Bob Can Meet
// https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

#include <algorithm>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> leftmostBuildingQueries(std::vector<int>& heights, std::vector<std::vector<int>>& queries) {
        int qn = (int)queries.size();
        std::vector<int> ans(qn, -1);
        std::vector<std::vector<std::pair<int, int>>> buckets(heights.size());
        for (int qi = 0; qi < qn; qi++) {
            int a = queries[qi][0], b = queries[qi][1];
            if (a > b) std::swap(a, b);
            if (a == b || heights[a] < heights[b]) {
                ans[qi] = b;
                continue;
            }
            buckets[b].push_back({heights[a], qi});
        }
        std::vector<std::pair<int, int>> st;
        for (int i = (int)heights.size() - 1; i >= 0; i--) {
            for (auto [h, qi] : buckets[i]) {
                int lo = 0, hi = (int)st.size() - 1, pos = -1;
                while (lo <= hi) {
                    int mid = (lo + hi) / 2;
                    if (st[mid].first > h) {
                        pos = st[mid].second;
                        lo = mid + 1;
                    } else hi = mid - 1;
                }
                ans[qi] = pos;
            }
            while (!st.empty() && st.back().first <= heights[i]) st.pop_back();
            st.push_back({heights[i], i});
        }
        return ans;
    }
};
