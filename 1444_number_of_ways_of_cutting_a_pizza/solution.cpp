#include <string>
#include <vector>

class Solution {
public:
    int ways(std::vector<std::string>& pizza, int k) {
        const int mod = 1000000007;
        int rows = (int)pizza.size(), cols = (int)pizza[0].size();
        std::vector<std::vector<int>> apples(rows + 1, std::vector<int>(cols + 1, 0));
        for (int r = rows - 1; r >= 0; --r)
            for (int c = cols - 1; c >= 0; --c)
                apples[r][c] = (pizza[r][c] == 'A') + apples[r + 1][c] + apples[r][c + 1] - apples[r + 1][c + 1];
        std::vector<std::vector<int>> dp(rows, std::vector<int>(cols, 0));
        for (int r = 0; r < rows; ++r)
            for (int c = 0; c < cols; ++c)
                dp[r][c] = apples[r][c] ? 1 : 0;
        for (int cut = 1; cut < k; ++cut) {
            std::vector<std::vector<int>> nxt(rows, std::vector<int>(cols, 0));
            for (int r = 0; r < rows; ++r) {
                for (int c = 0; c < cols; ++c) {
                    for (int nr = r + 1; nr < rows; ++nr)
                        if (apples[r][c] > apples[nr][c]) nxt[r][c] = (nxt[r][c] + dp[nr][c]) % mod;
                    for (int nc = c + 1; nc < cols; ++nc)
                        if (apples[r][c] > apples[r][nc]) nxt[r][c] = (nxt[r][c] + dp[r][nc]) % mod;
                }
            }
            dp = std::move(nxt);
        }
        return dp[0][0];
    }
};
