// LeetCode 2925 - Maximum Score After Applying Operations on a Tree
// https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

#include <functional>
#include <vector>

class Solution {
public:
    long long maximumScoreAfterOperations(std::vector<std::vector<int>>& edges, std::vector<int>& values) {
        int n = (int)values.size();
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        long long total = 0;
        for (int v : values) total += v;
        std::function<long long(int, int)> dfs = [&](int u, int p) {
            long long sumKids = 0;
            bool isLeaf = true;
            for (int v : g[u]) {
                if (v == p) continue;
                isLeaf = false;
                sumKids += dfs(v, u);
            }
            if (isLeaf) return (long long)values[u];
            return values[u] < sumKids ? (long long)values[u] : sumKids;
        };
        return total - dfs(0, -1);
    }
};
