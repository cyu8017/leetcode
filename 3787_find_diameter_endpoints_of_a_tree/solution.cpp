// LeetCode 3787 - Find Diameter Endpoints Of A Tree
// https://leetcode.com/problems/find-diameter-endpoints-of-a-tree/

#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    std::string findSpecialNodes(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        auto bfs = [&](int start) {
            std::vector<int> dist(n, -1);
            dist[start] = 0;
            std::vector<int> q;
            q.push_back(start);
            int far = start;
            for (int head = 0; head < (int)q.size(); head++) {
                int u = q[head];
                if (dist[u] > dist[far]) far = u;
                for (int v : g[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        q.push_back(v);
                    }
                }
            }
            return std::make_pair(far, dist);
        };
        auto [a, _] = bfs(0);
        auto [b, dist1] = bfs(a);
        auto [__, dist2] = bfs(b);
        (void)__;
        int d = dist1[b];
        std::string ans(n, '0');
        for (int i = 0; i < n; i++) {
            if (dist1[i] == d || dist2[i] == d) ans[i] = '1';
        }
        return ans;
    }
};
