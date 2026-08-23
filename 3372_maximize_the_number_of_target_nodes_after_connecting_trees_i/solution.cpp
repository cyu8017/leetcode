// LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

#include <queue>
#include <utility>
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

    int countWithin(std::vector<std::vector<int>>& g, int start, int k) {
        if (k < 0) return 0;
        int n = (int)g.size();
        std::vector<char> vis(n);
        std::queue<std::pair<int, int>> q;
        q.push({start, 0});
        vis[start] = 1;
        int cnt = 0;
        while (!q.empty()) {
            auto [u, d] = q.front();
            q.pop();
            cnt++;
            if (d == k) continue;
            for (int v : g[u]) {
                if (!vis[v]) {
                    vis[v] = 1;
                    q.push({v, d + 1});
                }
            }
        }
        return cnt;
    }

public:
    std::vector<int> maxTargetNodes(std::vector<std::vector<int>>& edges1, std::vector<std::vector<int>>& edges2, int k) {
        int n = (int)edges1.size() + 1;
        int m = (int)edges2.size() + 1;
        auto g1 = buildTree(n, edges1);
        auto g2 = buildTree(m, edges2);
        std::vector<int> cnt1(n);
        for (int i = 0; i < n; i++) cnt1[i] = countWithin(g1, i, k);
        int best2 = 0;
        if (k > 0) {
            for (int i = 0; i < m; i++) {
                int c = countWithin(g2, i, k - 1);
                if (c > best2) best2 = c;
            }
        }
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++) ans[i] = cnt1[i] + best2;
        return ans;
    }
};
