// LeetCode 3562 - Maximum Profit from Trading Stocks with Discounts
// https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

#include <algorithm>
#include <array>
#include <vector>

class Solution {
public:
    int maxProfit(int n, std::vector<int>& present, std::vector<int>& future,
                  std::vector<std::vector<int>>& hierarchy, int budget) {
        std::vector<std::vector<int>> g(n + 1);
        for (auto& e : hierarchy) g[e[0]].push_back(e[1]);

        auto dfs = [&](auto&& self, int u) -> std::vector<std::array<int, 2>> {
            std::vector<std::array<int, 2>> nxt(budget + 1);
            for (int v : g[u]) {
                auto fv = self(self, v);
                for (int j = budget; j >= 0; j--) {
                    for (int jv = 0; jv <= j; jv++) {
                        for (int pre = 0; pre < 2; pre++) {
                            nxt[j][pre] = std::max(nxt[j][pre], nxt[j - jv][pre] + fv[jv][pre]);
                        }
                    }
                }
            }
            std::vector<std::array<int, 2>> f(budget + 1);
            int price = future[u - 1];
            for (int j = 0; j <= budget; j++) {
                for (int pre = 0; pre < 2; pre++) {
                    int cost = present[u - 1] / (pre + 1);
                    if (j >= cost) {
                        int buyProfit = nxt[j - cost][1] + (price - cost);
                        f[j][pre] = std::max(nxt[j][0], buyProfit);
                    } else {
                        f[j][pre] = nxt[j][0];
                    }
                }
            }
            return f;
        };
        return dfs(dfs, 1)[budget][0];
    }
};
