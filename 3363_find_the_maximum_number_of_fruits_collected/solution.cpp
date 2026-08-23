// LeetCode 3363 - Find the Maximum Number of Fruits Collected
// https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

#include <vector>

class Solution {
public:
    int maxCollectedFruits(std::vector<std::vector<int>>& fruits) {
        int n = (int)fruits.size();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans += fruits[i][i];
            fruits[i][i] = 0;
        }
        const int neg = -(1 << 30);
        std::vector<std::vector<int>> dp2(n, std::vector<int>(n, neg));
        std::vector<std::vector<int>> dp3(n, std::vector<int>(n, neg));
        dp2[0][n - 1] = fruits[0][n - 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dp2[i][j] == neg) continue;
                for (int dj : {-1, 0, 1}) {
                    int ni = i + 1, nj = j + dj;
                    if (ni < n && nj >= 0 && nj < n && nj > ni) {
                        int v = dp2[i][j] + fruits[ni][nj];
                        if (v > dp2[ni][nj]) dp2[ni][nj] = v;
                    }
                }
            }
        }
        dp3[n - 1][0] = fruits[n - 1][0];
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < n; i++) {
                if (dp3[i][j] == neg) continue;
                for (int di : {-1, 0, 1}) {
                    int ni = i + di, nj = j + 1;
                    if (ni >= 0 && ni < n && nj < n && ni > nj) {
                        int v = dp3[i][j] + fruits[ni][nj];
                        if (v > dp3[ni][nj]) dp3[ni][nj] = v;
                    }
                }
            }
        }
        ans += dp2[n - 1][n - 1] + dp3[n - 1][n - 1];
        return ans;
    }
};
