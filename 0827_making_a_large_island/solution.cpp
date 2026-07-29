// LeetCode 0827 - Making A Large Island
// https://leetcode.com/problems/making-a-large-island/

#include <algorithm>
#include <functional>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int largestIsland(std::vector<std::vector<int>>& grid) {
        int n = static_cast<int>(grid.size());
        std::unordered_map<int, int> sizes{{0, 0}};
        int islandId = 2;

        std::function<int(int, int, int)> dfs = [&](int r, int c, int iid) -> int {
            if (r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1) {
                return 0;
            }
            grid[r][c] = iid;
            return 1 + dfs(r + 1, c, iid) + dfs(r - 1, c, iid) + dfs(r, c + 1, iid) +
                   dfs(r, c - 1, iid);
        };

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    sizes[islandId] = dfs(i, j, islandId);
                    ++islandId;
                }
            }
        }

        int ans = 0;
        for (auto& [_, v] : sizes) {
            ans = std::max(ans, v);
        }

        const int dr[4] = {1, -1, 0, 0};
        const int dc[4] = {0, 0, 1, -1};
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] != 0) {
                    continue;
                }
                std::unordered_set<int> seen;
                int total = 1;
                for (int k = 0; k < 4; ++k) {
                    int ni = i + dr[k], nj = j + dc[k];
                    if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                        int iid = grid[ni][nj];
                        if (iid > 1 && !seen.count(iid)) {
                            seen.insert(iid);
                            total += sizes[iid];
                        }
                    }
                }
                ans = std::max(ans, total);
            }
        }
        return ans;
    }
};
