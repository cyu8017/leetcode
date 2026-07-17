// LeetCode 1786 - Number of Restricted Paths From First to Last Node
// https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

#include <algorithm>
#include <climits>
#include <numeric>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int countRestrictedPaths(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<std::pair<int, int>>> adj(n + 1);
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }
        std::vector<long long> dist(n + 1, LLONG_MAX);
        dist[n] = 0;
        using Item = std::pair<long long, int>;
        std::priority_queue<Item, std::vector<Item>, std::greater<Item>> heap;
        heap.push({0, n});
        while (!heap.empty()) {
            auto [d, u] = heap.top();
            heap.pop();
            if (d != dist[u]) {
                continue;
            }
            for (const auto& [v, w] : adj[u]) {
                long long nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    heap.push({nd, v});
                }
            }
        }
        std::vector<int> order(n);
        std::iota(order.begin(), order.end(), 1);
        std::sort(order.begin(), order.end(), [&](int a, int b) { return dist[a] < dist[b]; });
        const long long MOD = 1000000007;
        std::vector<long long> cnt(n + 1, 0);
        cnt[n] = 1;
        for (int u : order) {
            if (u == n) {
                continue;
            }
            for (const auto& [v, w] : adj[u]) {
                if (dist[u] > dist[v]) {
                    cnt[u] = (cnt[u] + cnt[v]) % MOD;
                }
            }
        }
        return (int)cnt[1];
    }
};
