// LeetCode 2392 - Build a Matrix With Conditions
// https://leetcode.com/problems/build-a-matrix-with-conditions/

#include <queue>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> buildMatrix(int k, std::vector<std::vector<int>>& rowConditions, std::vector<std::vector<int>>& colConditions) {
        auto topo = [&](std::vector<std::vector<int>>& conds) -> std::vector<int> {
            std::vector<std::vector<int>> g(k + 1);
            std::vector<int> indeg(k + 1);
            for (auto& c : conds) {
                g[c[0]].push_back(c[1]);
                indeg[c[1]]++;
            }
            std::queue<int> q;
            for (int i = 1; i <= k; i++) if (indeg[i] == 0) q.push(i);
            std::vector<int> order;
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                order.push_back(u);
                for (int v : g[u]) {
                    if (--indeg[v] == 0) q.push(v);
                }
            }
            if ((int)order.size() != k) return {};
            return order;
        };
        auto rowOrder = topo(rowConditions);
        auto colOrder = topo(colConditions);
        if (rowOrder.empty() || colOrder.empty()) return {};
        std::vector<int> rowPos(k + 1), colPos(k + 1);
        for (int i = 0; i < k; i++) {
            rowPos[rowOrder[i]] = i;
            colPos[colOrder[i]] = i;
        }
        std::vector<std::vector<int>> ans(k, std::vector<int>(k));
        for (int v = 1; v <= k; v++) ans[rowPos[v]][colPos[v]] = v;
        return ans;
    }
};
