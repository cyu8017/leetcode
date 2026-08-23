// LeetCode 3786 - Total Sum of Interaction Cost in Tree Groups
// https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/

#include <array>
#include <cstdint>
#include <vector>

class Solution {
public:
    long long interactionCost(int n, std::vector<std::vector<int>>& edges, std::vector<int>& group) {
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::array<int, 21> total{};
        for (int x : group) total[x]++;
        std::vector<int> parent(n, -2);
        parent[0] = -1;
        std::vector<int> order = {0};
        for (int i = 0; i < (int)order.size(); i++) {
            int u = order[i];
            for (int v : g[u]) {
                if (parent[v] == -2) {
                    parent[v] = u;
                    order.push_back(v);
                }
            }
        }
        std::vector<std::array<int, 21>> count(n);
        int64_t ans = 0;
        for (int i = n - 1; i >= 0; i--) {
            int u = order[i];
            count[u][group[u]]++;
            for (int v : g[u]) {
                if (parent[v] != u) continue;
                for (int c = 1; c <= 20; c++) {
                    int x = count[v][c];
                    ans += (int64_t)x * (total[c] - x);
                    count[u][c] += x;
                }
            }
        }
        return ans;
    }
};
