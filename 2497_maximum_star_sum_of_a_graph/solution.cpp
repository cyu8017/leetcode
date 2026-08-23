// LeetCode 2497 - Maximum Star Sum of a Graph
// https://leetcode.com/problems/maximum-star-sum-of-a-graph/

#include <algorithm>
#include <functional>
#include <vector>

class Solution {
public:
    int maxStarSum(std::vector<int>& vals, std::vector<std::vector<int>>& edges, int k) {
        int n = (int)vals.size();
        std::vector<std::vector<int>> g(n);
        for (auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        int ans = vals[0];
        for (int i = 0; i < n; i++) {
            std::vector<int> neigh;
            for (int v : g[i]) {
                if (vals[v] > 0) neigh.push_back(vals[v]);
            }
            std::sort(neigh.begin(), neigh.end(), std::greater<int>());
            int sum = vals[i];
            for (int j = 0; j < (int)neigh.size() && j < k; j++) sum += neigh[j];
            if (sum > ans) ans = sum;
        }
        return ans;
    }
};
