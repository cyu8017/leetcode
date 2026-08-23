// LeetCode 3102 - Minimize Manhattan Distances
// https://leetcode.com/problems/minimize-manhattan-distances/

#include <algorithm>
#include <climits>
#include <map>
#include <vector>

class Solution {
public:
    int minimumDistance(std::vector<std::vector<int>>& points) {
        std::map<int, int> st1, st2;
        auto merge = [](std::map<int, int>& st, int x, int v) {
            st[x] += v;
            if (st[x] == 0) st.erase(x);
        };
        for (auto& p : points) {
            merge(st1, p[0] + p[1], 1);
            merge(st2, p[0] - p[1], 1);
        }
        int ans = INT_MAX;
        for (auto& p : points) {
            int x = p[0], y = p[1];
            merge(st1, x + y, -1);
            merge(st2, x - y, -1);
            ans = std::min(ans, std::max(st1.rbegin()->first - st1.begin()->first,
                                         st2.rbegin()->first - st2.begin()->first));
            merge(st1, x + y, 1);
            merge(st2, x - y, 1);
        }
        return ans;
    }
};
