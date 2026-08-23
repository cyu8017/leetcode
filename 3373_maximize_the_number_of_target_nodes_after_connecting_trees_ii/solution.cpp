// LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

#include <array>
#include <queue>
#include <vector>

class Solution {
    std::vector<std::vector<int>> buildTree(int n, std::vector<std::vector<int>>& edges) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        return g;
    }

    std::array<int, 2> bipartiteCount(std::vector<std::vector<int>>& g, std::vector<int>& color) {
        int n = (int)g.size();
        std::fill(color.begin(), color.end(), -1);
        std::queue<int> q;
        q.push(0);
        color[0] = 0;
        std::array<int, 2> cnt{{1, 0}};
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : g[u]) {
                if (color[v] == -1) {
                    color[v] = color[u] ^ 1;
                    cnt[color[v]]++;
                    q.push(v);
                }
            }
        }
        (void)n;
        return cnt;
    }

public:
    std::vector<int> maxTargetNodes(std::vector<std::vector<int>>& edges1, std::vector<std::vector<int>>& edges2) {
        int n = (int)edges1.size() + 1;
        int m = (int)edges2.size() + 1;
        auto g1 = buildTree(n, edges1);
        auto g2 = buildTree(m, edges2);
        std::vector<int> color1(n), color2(m);
        auto c1 = bipartiteCount(g1, color1);
        auto c2 = bipartiteCount(g2, color2);
        int best2 = std::max(c2[0], c2[1]);
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++) ans[i] = c1[color1[i]] + best2;
        return ans;
    }
};
