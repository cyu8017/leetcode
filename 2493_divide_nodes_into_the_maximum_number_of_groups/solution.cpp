// LeetCode 2493 - Divide Nodes Into the Maximum Number of Groups
// https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

#include <queue>
#include <vector>

class Solution {
public:
    int magnificentSets(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> g(n + 1);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::vector<int> color(n + 1, -1);
        std::vector<std::vector<int>> components;
        for (int i = 1; i <= n; i++) {
            if (color[i] != -1) continue;
            std::vector<int> comp;
            std::queue<int> q;
            q.push(i);
            color[i] = 0;
            bool bipartite = true;
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                comp.push_back(u);
                for (int v : g[u]) {
                    if (color[v] == -1) {
                        color[v] = color[u] ^ 1;
                        q.push(v);
                    } else if (color[v] == color[u]) {
                        bipartite = false;
                    }
                }
            }
            if (!bipartite) return -1;
            components.push_back(comp);
        }
        auto bfsDepth = [&](int start) {
            std::vector<int> dist(n + 1, -1);
            std::queue<int> q;
            q.push(start);
            dist[start] = 1;
            int best = 1;
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                if (dist[u] > best) best = dist[u];
                for (int v : g[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        q.push(v);
                    }
                }
            }
            return best;
        };
        int ans = 0;
        for (auto& comp : components) {
            int best = 0;
            for (int u : comp) {
                int d = bfsDepth(u);
                if (d > best) best = d;
            }
            ans += best;
        }
        return ans;
    }
};
