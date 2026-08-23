// LeetCode 2477 - Minimum Fuel Cost to Report to the Capital
// https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

#include <functional>
#include <vector>

class Solution {
public:
    long long minimumFuelCost(std::vector<std::vector<int>>& roads, int seats) {
        int n = (int)roads.size() + 1;
        std::vector<std::vector<int>> g(n);
        for (auto& r : roads) {
            g[r[0]].push_back(r[1]);
            g[r[1]].push_back(r[0]);
        }
        long long ans = 0;
        std::function<int(int, int)> dfs = [&](int u, int p) {
            int people = 1;
            for (int v : g[u]) {
                if (v != p) people += dfs(v, u);
            }
            if (u != 0) ans += (people + seats - 1) / seats;
            return people;
        };
        dfs(0, -1);
        return ans;
    }
};
