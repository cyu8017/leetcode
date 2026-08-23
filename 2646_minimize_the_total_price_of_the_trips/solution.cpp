// LeetCode 2646 - Minimize the Total Price of the Trips
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

#include <vector>
#include <functional>
#include <algorithm>

class Solution {
public:
    int minimumTotalPrice(int n, std::vector<std::vector<int>>& edges, std::vector<int>& price, std::vector<std::vector<int>>& trips) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) { g[e[0]].push_back(e[1]); g[e[1]].push_back(e[0]); }
        std::vector<int> cnt(n);
        std::function<bool(int,int,int)> path = [&](int u, int p, int target) -> bool {
            if (u == target) { cnt[u]++; return true; }
            for (int v : g[u]) {
                if (v == p) continue;
                if (path(v, u, target)) { cnt[u]++; return true; }
            }
            return false;
        };
        for (auto& t : trips) path(t[0], -1, t[1]);
        std::function<std::pair<int,int>(int,int)> dfs = [&](int u, int p) -> std::pair<int,int> {
            int full = price[u] * cnt[u], half = full / 2;
            for (int v : g[u]) {
                if (v == p) continue;
                auto [nf, hf] = dfs(v, u);
                full += std::min(nf, hf);
                half += nf;
            }
            return {full, half};
        };
        auto [a, b] = dfs(0, -1);
        return std::min(a, b);
    }
};
