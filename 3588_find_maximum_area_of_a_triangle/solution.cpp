// LeetCode 3588 - Find Maximum Area of a Triangle
// https://leetcode.com/problems/find-maximum-area-of-a-triangle/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long maxArea(std::vector<std::vector<int>>& coords) {
        auto calc = [&]() -> long long {
            int mn = 1e9, mx = 0;
            std::unordered_map<int, int> f, g;
            for (auto& c : coords) {
                int x = c[0], y = c[1];
                mn = std::min(mn, x);
                mx = std::max(mx, x);
                if (f.count(x)) {
                    f[x] = std::min(f[x], y);
                    g[x] = std::max(g[x], y);
                } else {
                    f[x] = y;
                    g[x] = y;
                }
            }
            long long ans = 0;
            for (auto& [x, y] : f) {
                int d = g[x] - y;
                ans = std::max(ans, 1LL * d * std::max(mx - x, x - mn));
            }
            return ans;
        };
        long long ans = calc();
        for (auto& c : coords) std::swap(c[0], c[1]);
        ans = std::max(ans, calc());
        return ans > 0 ? ans : -1;
    }
};
