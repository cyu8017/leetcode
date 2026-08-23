// LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
// https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long getMaxFunctionValue(std::vector<int>& receiver, long long k) {
        int n = (int)receiver.size();
        const int LOG = 36;
        std::vector<std::vector<int>> up(LOG, std::vector<int>(n));
        std::vector<std::vector<long long>> sum(LOG, std::vector<long long>(n));
        for (int i = 0; i < n; i++) {
            up[0][i] = receiver[i];
            sum[0][i] = receiver[i];
        }
        for (int j = 1; j < LOG; j++) {
            for (int i = 0; i < n; i++) {
                int mid = up[j - 1][i];
                up[j][i] = up[j - 1][mid];
                sum[j][i] = sum[j - 1][i] + sum[j - 1][mid];
            }
        }
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            int cur = i;
            long long total = i;
            long long kk = k;
            for (int j = 0; j < LOG; j++) {
                if (kk & (1LL << j)) {
                    total += sum[j][cur];
                    cur = up[j][cur];
                }
            }
            ans = std::max(ans, total);
        }
        return ans;
    }
};
