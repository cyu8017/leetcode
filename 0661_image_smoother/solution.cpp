// LeetCode 0661 - Image Smoother
// https://leetcode.com/problems/image-smoother/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> imageSmoother(std::vector<std::vector<int>>& img) {
        const int m = static_cast<int>(img.size());
        const int n = static_cast<int>(img[0].size());
        std::vector<std::vector<int>> out(m, std::vector<int>(n, 0));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int total = 0;
                int count = 0;
                for (int di = -1; di <= 1; ++di) {
                    for (int dj = -1; dj <= 1; ++dj) {
                        const int ni = i + di;
                        const int nj = j + dj;
                        if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
                            total += img[ni][nj];
                            ++count;
                        }
                    }
                }
                out[i][j] = total / count;
            }
        }
        return out;
    }
};
