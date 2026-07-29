// LeetCode 1992 - Find All Groups of Farmland
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> findFarmland(std::vector<std::vector<int>>& land) {
        int m = (int)land.size(), n = (int)land[0].size();
        std::vector<std::vector<int>> ans;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (land[i][j] == 1 && (i == 0 || land[i - 1][j] == 0) && (j == 0 || land[i][j - 1] == 0)) {
                    int r = i, c = j;
                    while (r + 1 < m && land[r + 1][j] == 1) r++;
                    while (c + 1 < n && land[i][c + 1] == 1) c++;
                    ans.push_back({i, j, r, c});
                }
            }
        }
        return ans;
    }
};
