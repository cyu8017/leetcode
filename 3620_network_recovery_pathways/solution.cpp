// LeetCode 3620 - Network Recovery Pathways
// https://leetcode.com/problems/network-recovery-pathways/

#include <algorithm>
#include <climits>
#include <queue>
#include <vector>

class Solution {
public:
    int findMaxPathScore(std::vector<std::vector<int>>& edges, std::vector<bool>& online, long long k) {
        int n = (int)online.size();
        std::vector<std::vector<std::pair<int, int>>> g(n);
        int l = INT_MAX, r = 0;
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            if (!online[u] || !online[v]) continue;
            g[u].push_back({v, w});
            l = std::min(l, w);
            r = std::max(r, w);
        }
        if (l == INT_MAX) return -1;
        auto check = [&](int mid) {
            const int INF = INT_MAX / 2;
            std::vector<int> dist(n, INF);
            dist[0] = 0;
            using P = std::pair<int, int>;
            std::priority_queue<P, std::vector<P>, std::greater<P>> pq;
            pq.push({0, 0});
            while (!pq.empty()) {
                auto [d, u] = pq.top();
                pq.pop();
                if ((long long)d > k) return false;
                if (u == n - 1) return true;
                if (dist[u] < d) continue;
                for (auto [v, w] : g[u]) {
                    if (w < mid) continue;
                    int nd = d + w;
                    if (nd < dist[v]) {
                        dist[v] = nd;
                        pq.push({nd, v});
                    }
                }
            }
            return false;
        };
        while (l < r) {
            int mid = (l + r + 1) >> 1;
            if (check(mid)) l = mid;
            else r = mid - 1;
        }
        return check(l) ? l : -1;
    }
};
