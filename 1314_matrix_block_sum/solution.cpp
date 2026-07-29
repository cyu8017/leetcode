#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> matrixBlockSum(std::vector<std::vector<int>>& mat, int k) {
        int m = (int)mat.size(), n = (int)mat[0].size();
        std::vector<std::vector<int>> prefix(m + 1, std::vector<int>(n + 1, 0));
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                prefix[i + 1][j + 1] = mat[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j];
        auto sum = [&](int r1, int c1, int r2, int c2) {
            return prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1];
        };
        std::vector<std::vector<int>> answer(m, std::vector<int>(n));
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j) {
                int r1 = std::max(0, i - k), c1 = std::max(0, j - k);
                int r2 = std::min(m - 1, i + k), c2 = std::min(n - 1, j + k);
                answer[i][j] = sum(r1, c1, r2, c2);
            }
        return answer;
    }
};
