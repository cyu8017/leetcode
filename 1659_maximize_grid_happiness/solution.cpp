// LeetCode 1659 - Maximize Grid Happiness
// https://leetcode.com/problems/maximize-grid-happiness/

#include <algorithm>
#include <cstring>
#include <vector>

class Solution {
    static int pairCost(int a, int b) {
        if (!a || !b) {
            return 0;
        }
        return (a == 1 ? -30 : 20) + (b == 1 ? -30 : 20);
    }

public:
    int getMaxGridHappiness(int m, int n, int introvertsCount, int extrovertsCount) {
        int states = 1;
        for (int t = 0; t < n; ++t) {
            states *= 3;
        }
        std::vector<std::vector<int>> cells(states, std::vector<int>(n));
        std::vector<int> intro(states), extro(states), row(states);
        for (int s = 0; s < states; ++s) {
            int x = s;
            for (int j = 0; j < n; ++j) {
                cells[s][j] = x % 3;
                x /= 3;
            }
            int val = 0;
            for (int j = 0; j < n; ++j) {
                int z = cells[s][j];
                if (z == 1) {
                    ++intro[s];
                    val += 120;
                } else if (z == 2) {
                    ++extro[s];
                    val += 40;
                }
            }
            for (int j = 1; j < n; ++j) {
                val += pairCost(cells[s][j - 1], cells[s][j]);
            }
            row[s] = val;
        }
        std::vector<std::vector<int>> compat(states, std::vector<int>(states));
        for (int a = 0; a < states; ++a) {
            for (int b = 0; b < states; ++b) {
                int v = 0;
                for (int j = 0; j < n; ++j) {
                    v += pairCost(cells[a][j], cells[b][j]);
                }
                compat[a][b] = v;
            }
        }

        int dims = (m + 1) * states * (introvertsCount + 1) * (extrovertsCount + 1);
        std::vector<int> memo(dims, -1);
        auto idx = [&](int r, int prev, int i, int e) {
            return (((r * states + prev) * (introvertsCount + 1) + i) * (extrovertsCount + 1) + e);
        };
        auto dfs = [&](auto&& self, int r, int prev, int i, int e) -> int {
            if (r == m) {
                return 0;
            }
            int id = idx(r, prev, i, e);
            if (memo[id] != -1) {
                return memo[id];
            }
            int best = 0;
            for (int s = 0; s < states; ++s) {
                if (intro[s] > i || extro[s] > e) {
                    continue;
                }
                best = std::max(best, row[s] + compat[prev][s] + self(self, r + 1, s, i - intro[s], e - extro[s]));
            }
            return memo[id] = best;
        };
        return dfs(dfs, 0, 0, introvertsCount, extrovertsCount);
    }
};
