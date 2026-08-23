// LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
// https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

#include <queue>
#include <vector>

class Solution {
public:
    int minMaxWeight(int n, std::vector<std::vector<int>>& edges, int threshold) {
        (void)threshold;
        auto ok = [&](int mid) {
            std::vector<std::vector<int>> g(n);
            for (auto& e : edges) {
                int a = e[0], b = e[1], w = e[2];
                if (w <= mid) g[b].push_back(a);
            }
            std::vector<char> vis(n);
            std::queue<int> q;
            q.push(0);
            vis[0] = 1;
            int cnt = 1;
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                for (int v : g[u]) {
                    if (!vis[v]) {
                        vis[v] = 1;
                        cnt++;
                        q.push(v);
                    }
                }
            }
            return cnt == n;
        };
        int lo = 1, hi = 1000001, ans = -1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ok(mid)) {
                ans = mid;
                hi = mid;
            } else lo = mid + 1;
        }
        return ans;
    }
};
