// LeetCode 3585 - Find Weighted Median Node in Tree
// https://leetcode.com/problems/find-weighted-median-node-in-tree/

#include <algorithm>
#include <queue>
#include <vector>

class Solution {
public:
    std::vector<int> findMedian(int n, std::vector<std::vector<int>>& edges, std::vector<std::vector<int>>& queries) {
        struct Edge { int to, w; };
        std::vector<std::vector<Edge>> g(n);
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].push_back({v, w});
            g[v].push_back({u, w});
        }
        std::vector<int> ans(queries.size());
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            int u = queries[qi][0], v = queries[qi][1];
            std::vector<int> parent(n, -2), pw(n);
            parent[u] = -1;
            std::queue<int> q;
            q.push(u);
            while (!q.empty()) {
                int x = q.front();
                q.pop();
                if (x == v) break;
                for (auto& e : g[x]) {
                    if (parent[e.to] == -2) {
                        parent[e.to] = x;
                        pw[e.to] = e.w;
                        q.push(e.to);
                    }
                }
            }
            std::vector<int> nodes{v}, weights;
            int cur = v;
            while (cur != u) {
                weights.push_back(pw[cur]);
                cur = parent[cur];
                nodes.push_back(cur);
            }
            std::reverse(nodes.begin(), nodes.end());
            std::reverse(weights.begin(), weights.end());
            int total = 0;
            for (int w : weights) total += w;
            int need = (total + 1) / 2, sum = 0, med = u;
            for (int i = 0; i < (int)weights.size(); i++) {
                sum += weights[i];
                med = nodes[i + 1];
                if (sum >= need) break;
            }
            ans[qi] = med;
        }
        return ans;
    }
};
