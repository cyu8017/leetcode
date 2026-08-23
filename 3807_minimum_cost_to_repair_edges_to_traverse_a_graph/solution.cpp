// LeetCode 3807 - Minimum Cost To Repair Edges To Traverse A Graph
// https://leetcode.com/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minCost(int n, std::vector<std::vector<int>>& edges, int k) {
        std::sort(edges.begin(), edges.end(), [](auto& a, auto& b) { return a[2] < b[2]; });
        auto check = [&](int idx) {
            std::vector<std::vector<int>> g(n);
            for (int i = 0; i <= idx; i++) {
                g[edges[i][0]].push_back(edges[i][1]);
                g[edges[i][1]].push_back(edges[i][0]);
            }
            std::vector<int> q = {0};
            std::vector<char> vis(n, 0);
            vis[0] = 1;
            int dist = 0;
            while (!q.empty()) {
                std::vector<int> nq;
                for (int u : q) {
                    if (u == n - 1) return dist <= k;
                    for (int v : g[u]) {
                        if (!vis[v]) {
                            vis[v] = 1;
                            nq.push_back(v);
                        }
                    }
                }
                q = std::move(nq);
                dist++;
            }
            return false;
        };
        int m = (int)edges.size();
        if (m == 0) return -1;
        int l = 0, r = m - 1;
        while (l < r) {
            int mid = (l + r) >> 1;
            if (check(mid)) r = mid;
            else l = mid + 1;
        }
        if (check(l)) return edges[l][2];
        return -1;
    }
};
