// LeetCode 0959 - Regions Cut By Slashes
// https://leetcode.com/problems/regions-cut-by-slashes/

#include <string>
#include <vector>

class Solution {
public:
    int regionsBySlashes(std::vector<std::string>& grid) {
        int n = (int)grid.size();
        std::vector<int> parent(n * n * 4);
        for (int i = 0; i < (int)parent.size(); i++) parent[i] = i;
        auto find = [&](auto&& self, int x) -> int {
            return parent[x] == x ? x : parent[x] = self(self, parent[x]);
        };
        auto unite = [&](int a, int b) { parent[find(find, a)] = find(find, b); };
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                int root = 4 * (r * n + c);
                char ch = grid[r][c];
                if (ch == '/') {
                    unite(root + 0, root + 3);
                    unite(root + 1, root + 2);
                } else if (ch == '\\') {
                    unite(root + 0, root + 1);
                    unite(root + 2, root + 3);
                } else {
                    unite(root + 0, root + 1);
                    unite(root + 1, root + 2);
                    unite(root + 2, root + 3);
                }
                if (r + 1 < n) unite(root + 2, root + 4 * n + 0);
                if (c + 1 < n) unite(root + 1, root + 4 + 3);
            }
        }
        int ans = 0;
        for (int i = 0; i < (int)parent.size(); i++) if (find(find, i) == i) ans++;
        return ans;
    }
};
