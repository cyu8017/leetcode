// LeetCode 1766 - Tree of Coprimes
// https://leetcode.com/problems/tree-of-coprimes/

#include <numeric>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<int> getCoprimes(std::vector<int>& nums, std::vector<std::vector<int>>& edges) {
        int n = (int)nums.size();
        adj.assign(n, {});
        for (const auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        vals = nums;
        ans.assign(n, -1);
        path.assign(51, {});
        dfs(0, -1, 0);
        return ans;
    }

private:
    std::vector<std::vector<int>> adj;
    std::vector<int> vals;
    std::vector<int> ans;
    std::vector<std::vector<std::pair<int, int>>> path;

    void dfs(int node, int parent, int depth) {
        int bestDepth = -1;
        int bestNode = -1;
        int val = vals[node];
        for (int d = 1; d <= 50; d++) {
            if (std::gcd(val, d) == 1 && !path[d].empty()) {
                const auto& cand = path[d].back();
                if (cand.first > bestDepth) {
                    bestDepth = cand.first;
                    bestNode = cand.second;
                }
            }
        }
        ans[node] = bestNode;
        path[val].push_back({depth, node});
        for (int nxt : adj[node]) {
            if (nxt != parent) {
                dfs(nxt, node, depth + 1);
            }
        }
        path[val].pop_back();
    }
};
