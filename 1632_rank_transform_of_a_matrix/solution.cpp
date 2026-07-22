// LeetCode 1632 - Rank Transform of a Matrix
// https://leetcode.com/problems/rank-transform-of-a-matrix/

#include <algorithm>
#include <map>
#include <unordered_map>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> matrixRankTransform(std::vector<std::vector<int>>& matrix) {
        const int m = static_cast<int>(matrix.size());
        const int n = static_cast<int>(matrix[0].size());
        std::map<int, std::vector<std::pair<int, int>>> groups;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                groups[matrix[i][j]].push_back({i, j});
            }
        }
        std::vector<int> rank(m + n, 0);
        std::vector<std::vector<int>> ans(m, std::vector<int>(n, 0));
        for (auto& [value, cells] : groups) {
            (void)value;
            std::unordered_map<int, int> parent;
            auto find = [&](auto&& self, int x) -> int {
                if (!parent.count(x)) {
                    parent[x] = x;
                }
                if (parent[x] != x) {
                    parent[x] = self(self, parent[x]);
                }
                return parent[x];
            };
            for (auto [i, j] : cells) {
                const int a = find(find, i);
                const int b = find(find, m + j);
                parent[a] = b;
            }
            std::unordered_map<int, int> best;
            for (auto [i, j] : cells) {
                const int root = find(find, i);
                best[root] = std::max(best[root], std::max(rank[i], rank[m + j]));
            }
            for (auto [i, j] : cells) {
                ans[i][j] = best[find(find, i)] + 1;
            }
            for (auto [i, j] : cells) {
                rank[i] = std::max(rank[i], ans[i][j]);
                rank[m + j] = std::max(rank[m + j], ans[i][j]);
            }
        }
        return ans;
    }
};
