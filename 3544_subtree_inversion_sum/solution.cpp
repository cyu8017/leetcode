// LeetCode 3544 - Subtree Inversion Sum
// https://leetcode.com/problems/subtree-inversion-sum/

#include <vector>
#include <map>
#include <tuple>

class Solution {
public:
    long long subtreeInversionSum(std::vector<std::vector<int>>& edges, std::vector<int>& nums, int k) {
        int n = (int)edges.size() + 1;
        std::vector<std::vector<int>> graph(n);
        for (auto& e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        std::vector<int> parent(n, -1);
        std::map<std::tuple<int, int, bool>, long long> memo;
        auto dp = [&](auto&& self, int u, int steps, bool inv) -> long long {
            auto key = std::make_tuple(u, steps, inv);
            if (memo.count(key)) return memo[key];
            long long num = nums[u];
            if (inv) num = -num;
            long long negNum = -num;
            for (int v : graph[u]) {
                if (v == parent[u]) continue;
                parent[v] = u;
                int ns = steps + 1;
                if (ns > k) ns = k;
                num += self(self, v, ns, inv);
                if (steps == k) negNum += self(self, v, 1, !inv);
            }
            long long res = num;
            if (steps == k && negNum > res) res = negNum;
            return memo[key] = res;
        };
        return dp(dp, 0, k, false);
    }
};
