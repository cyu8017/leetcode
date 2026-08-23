// LeetCode 3924 - Minimum Threshold Path With Limited Heavy Edges
// https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/

#include <algorithm>
#include <deque>
#include <vector>

class Solution {
public:
    int minThreshold(int n, std::vector<std::vector<int>>& edges, int source, int target, int k) {
        if (source == target) return 0;
        std::vector<std::vector<std::pair<int, int>>> g(n);
        int maxWeight = 0;
        for (auto& e : edges) {
            g[e[0]].push_back({e[1], e[2]});
            g[e[1]].push_back({e[0], e[2]});
            maxWeight = std::max(maxWeight, e[2]);
        }
        auto can = [&](int threshold) {
            const int inf = 1000000000;
            std::vector<int> dist(n, inf);
            dist[source] = 0;
            std::deque<int> dq;
            dq.push_back(source);
            while (!dq.empty()) {
                int u = dq.front();
                dq.pop_front();
                for (auto& [to, weight] : g[u]) {
                    int cost = weight > threshold ? 1 : 0;
                    if (dist[u] + cost >= dist[to] || dist[u] + cost > k) continue;
                    dist[to] = dist[u] + cost;
                    if (cost == 0) dq.push_front(to);
                    else dq.push_back(to);
                }
            }
            return dist[target] <= k;
        };
        if (!can(maxWeight)) return -1;
        int lo = 0, hi = maxWeight;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (can(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
};
