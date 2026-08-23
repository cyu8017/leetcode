// LeetCode 2467 - Most Profitable Path in a Tree
// https://leetcode.com/problems/most-profitable-path-in-a-tree/

#include <climits>
#include <functional>
#include <vector>

class Solution {
public:
    int mostProfitablePath(std::vector<std::vector<int>>& edges, int bob, std::vector<int>& amount) {
        int n = (int)amount.size();
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        std::vector<int> bobTime(n, n);
        std::function<bool(int, int, int)> findBob = [&](int u, int p, int t) -> bool {
            if (u == 0) {
                bobTime[u] = t;
                return true;
            }
            for (int v : g[u]) {
                if (v == p) continue;
                if (findBob(v, u, t + 1)) {
                    bobTime[u] = t;
                    return true;
                }
            }
            return false;
        };
        findBob(bob, -1, 0);
        int ans = INT_MIN;
        std::function<void(int, int, int, int)> dfs = [&](int u, int p, int t, int income) {
            int cur = amount[u];
            if (t > bobTime[u]) cur = 0;
            else if (t == bobTime[u]) cur /= 2;
            income += cur;
            bool isLeaf = true;
            for (int v : g[u]) {
                if (v != p) {
                    isLeaf = false;
                    dfs(v, u, t + 1, income);
                }
            }
            if (isLeaf && income > ans) ans = income;
        };
        dfs(0, -1, 0, 0);
        return ans;
    }
};
