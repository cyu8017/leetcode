// LeetCode 3613 - Minimize Maximum Component Cost
// https://leetcode.com/problems/minimize-maximum-component-cost/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minCost(int n, std::vector<std::vector<int>>& edges, int k) {
        std::vector<int> p(n);
        for (int i = 0; i < n; i++) p[i] = i;
        auto find = [&](auto&& self, int x) -> int {
            return p[x] == x ? x : p[x] = self(self, p[x]);
        };
        if (k == n) return 0;
        std::sort(edges.begin(), edges.end(), [](auto& a, auto& b) { return a[2] < b[2]; });
        int cnt = n;
        for (auto& e : edges) {
            int pu = find(find, e[0]), pv = find(find, e[1]);
            if (pu != pv) {
                p[pu] = pv;
                if (--cnt <= k) return e[2];
            }
        }
        return 0;
    }
};
