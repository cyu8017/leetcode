// LeetCode 3030 - Find the Grid of Region Average
// https://leetcode.com/problems/find-the-grid-of-region-average/

#include <cstdlib>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> resultGrid(std::vector<std::vector<int>>& image, int threshold) {
        int n = (int)image.size(), m = (int)image[0].size();
        std::vector<std::vector<int>> ans(n, std::vector<int>(m, 0));
        std::vector<std::vector<int>> ct(n, std::vector<int>(m, 0));
        for (int i = 0; i + 2 < n; i++) {
            for (int j = 0; j + 2 < m; j++) {
                bool region = true;
                for (int k = 0; k < 3; k++)
                    for (int l = 0; l < 2; l++)
                        region = region && std::abs(image[i + k][j + l] - image[i + k][j + l + 1]) <= threshold;
                for (int k = 0; k < 2; k++)
                    for (int l = 0; l < 3; l++)
                        region = region && std::abs(image[i + k][j + l] - image[i + k + 1][j + l]) <= threshold;
                if (region) {
                    int tot = 0;
                    for (int k = 0; k < 3; k++)
                        for (int l = 0; l < 3; l++)
                            tot += image[i + k][j + l];
                    for (int k = 0; k < 3; k++)
                        for (int l = 0; l < 3; l++) {
                            ct[i + k][j + l]++;
                            ans[i + k][j + l] += tot / 9;
                        }
                }
            }
        }
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                if (ct[i][j] == 0) ans[i][j] = image[i][j];
                else ans[i][j] /= ct[i][j];
            }
        return ans;
    }
};
